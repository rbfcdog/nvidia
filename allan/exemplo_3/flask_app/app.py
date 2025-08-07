from flask import Flask, render_template, request, jsonify, send_file, flash, redirect, url_for
import os
import uuid
import shutil
from werkzeug.utils import secure_filename
import subprocess
import markdown
import pdfkit
from datetime import datetime
import threading
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['REPORTS_FOLDER'] = 'reports'
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # 100MB max file size

# Ensure directories exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['REPORTS_FOLDER'], exist_ok=True)
os.makedirs('agents/input', exist_ok=True)
os.makedirs('agents/outputs', exist_ok=True)
os.makedirs('agents/outputs/report_sections', exist_ok=True)

ALLOWED_EXTENSIONS = {'txt', 'log', 'xml', 'json', 'csv', 'nmap', 'scan'}

# Store analysis status
analysis_status = {}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def compile_scan_files(session_id):
    """Compile uploaded scan files into recon_raw_output.txt"""
    upload_path = os.path.join(app.config['UPLOAD_FOLDER'], session_id)
    compiled_content = []
    
    compiled_content.append(f"# Compiled Security Scan Report - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    compiled_content.append("=" * 80 + "\n\n")
    
    for filename in os.listdir(upload_path):
        file_path = os.path.join(upload_path, filename)
        if os.path.isfile(file_path):
            compiled_content.append(f"## File: {filename}\n")
            compiled_content.append("-" * 40 + "\n")
            
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    compiled_content.append(content)
                    compiled_content.append("\n\n")
            except Exception as e:
                compiled_content.append(f"Error reading file: {str(e)}\n\n")
    
    # Write compiled content
    output_path = 'agents/input/recon_raw_output.txt'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.writelines(compiled_content)
    
    return output_path

def run_security_analysis(session_id):
    """Run the security analysis in background"""
    try:
        analysis_status[session_id] = {'status': 'running', 'progress': 10}
        
        # Change to agents directory
        original_dir = os.getcwd()
        os.chdir('agents')
        
        analysis_status[session_id]['progress'] = 30
        
        # Import and run the analysis
        from agents.crew_main import run_optimized_analysis  # Removido 'agents.' do import
        
        analysis_status[session_id]['progress'] = 50
        
        result = run_optimized_analysis()
        
        analysis_status[session_id]['progress'] = 80
        
        if result:
            # Convert markdown to PDF (volta para o diretório original primeiro)
            os.chdir(original_dir)
            convert_to_pdf(session_id)
            analysis_status[session_id] = {'status': 'completed', 'progress': 100}
        else:
            analysis_status[session_id] = {'status': 'error', 'error': 'Analysis failed'}
            
    except Exception as e:
        analysis_status[session_id] = {'status': 'error', 'error': str(e)}
    finally:
        os.chdir(original_dir)

def convert_to_pdf(session_id):
    """Convert markdown report to PDF"""
    try:
        # Caminho absoluto para o arquivo markdown
        md_path = os.path.join('agents', 'outputs', 'pentest_report.md')
        
        # Verificar se o arquivo existe
        if not os.path.exists(md_path):
            # Tentar caminhos alternativos
            alternative_paths = [
                'outputs/pentest_report.md',
                'agents/outputs/pentest_report.md',
                os.path.join(os.getcwd(), 'agents', 'outputs', 'pentest_report.md')
            ]
            
            found = False
            for alt_path in alternative_paths:
                if os.path.exists(alt_path):
                    md_path = alt_path
                    found = True
                    break
            
            if not found:
                # Listar arquivos para debug
                debug_info = []
                if os.path.exists('agents/outputs'):
                    debug_info.append(f"Files in agents/outputs: {os.listdir('agents/outputs')}")
                if os.path.exists('outputs'):
                    debug_info.append(f"Files in outputs: {os.listdir('outputs')}")
                
                raise Exception(f"Markdown report not found. Searched paths: {[md_path] + alternative_paths}. Debug: {debug_info}")
        
        with open(md_path, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        # Convert to HTML
        html_content = markdown.markdown(md_content, extensions=['tables', 'fenced_code'])
        
        # Add CSS styling
        styled_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>Penetration Test Report</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 40px; line-height: 1.6; }}
                h1 {{ color: #2c3e50; border-bottom: 2px solid #3498db; }}
                h2 {{ color: #34495e; border-bottom: 1px solid #bdc3c7; }}
                h3 {{ color: #7f8c8d; }}
                table {{ border-collapse: collapse; width: 100%; margin: 20px 0; }}
                th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
                th {{ background-color: #f2f2f2; }}
                code {{ background-color: #f8f9fa; padding: 2px 4px; border-radius: 3px; }}
                pre {{ background-color: #f8f9fa; padding: 10px; border-radius: 5px; overflow-x: auto; }}
                .critical {{ color: #e74c3c; font-weight: bold; }}
                .high {{ color: #f39c12; font-weight: bold; }}
                .medium {{ color: #f1c40f; font-weight: bold; }}
                .low {{ color: #27ae60; font-weight: bold; }}
            </style>
        </head>
        <body>
            {html_content}
        </body>
        </html>
        """
        
        # Convert to PDF
        pdf_path = os.path.join(app.config['REPORTS_FOLDER'], f'pentest_report_{session_id}.pdf')
        
        options = {
            'page-size': 'A4',
            'margin-top': '0.75in',
            'margin-right': '0.75in',
            'margin-bottom': '0.75in',
            'margin-left': '0.75in',
            'encoding': "UTF-8",
            'no-outline': None
        }
        
        pdfkit.from_string(styled_html, pdf_path, options=options)
        
        return pdf_path
        
    except Exception as e:
        raise Exception(f"PDF conversion failed: {str(e)}")

# Também adicione uma função de debug para verificar arquivos
@app.route('/debug/<session_id>')
def debug_files(session_id):
    """Debug endpoint to check file structure"""
    debug_info = {
        'current_dir': os.getcwd(),
        'session_id': session_id,
        'agents_exists': os.path.exists('agents'),
        'agents_outputs_exists': os.path.exists('agents/outputs'),
        'analysis_status': analysis_status.get(session_id, 'not_found')
    }
    
    if os.path.exists('agents'):
        debug_info['agents_contents'] = os.listdir('agents')
    
    if os.path.exists('agents/outputs'):
        debug_info['outputs_contents'] = os.listdir('agents/outputs')
        
    if os.path.exists('agents/outputs/pentest_report.md'):
        debug_info['pentest_report_exists'] = True
        with open('agents/outputs/pentest_report.md', 'r') as f:
            debug_info['pentest_report_size'] = len(f.read())
    else:
        debug_info['pentest_report_exists'] = False
    
    return jsonify(debug_info)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_files():
    if 'files[]' not in request.files:
        return jsonify({'error': 'No files uploaded'}), 400
    
    files = request.files.getlist('files[]')
    
    if not files or all(f.filename == '' for f in files):
        return jsonify({'error': 'No files selected'}), 400
    
    # Generate session ID
    session_id = str(uuid.uuid4())
    session_path = os.path.join(app.config['UPLOAD_FOLDER'], session_id)
    os.makedirs(session_path, exist_ok=True)
    
    uploaded_files = []
    
    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(session_path, filename)
            file.save(file_path)
            uploaded_files.append(filename)
    
    if not uploaded_files:
        shutil.rmtree(session_path)
        return jsonify({'error': 'No valid files uploaded'}), 400
    
    # Compile files
    try:
        compile_scan_files(session_id)
        return jsonify({
            'session_id': session_id,
            'uploaded_files': uploaded_files,
            'message': 'Files uploaded and compiled successfully'
        })
    except Exception as e:
        shutil.rmtree(session_path)
        return jsonify({'error': f'Compilation failed: {str(e)}'}), 500

@app.route('/analyze/<session_id>', methods=['POST'])
def start_analysis(session_id):
    session_path = os.path.join(app.config['UPLOAD_FOLDER'], session_id)
    
    if not os.path.exists(session_path):
        return jsonify({'error': 'Invalid session ID'}), 404
    
    # Start analysis in background
    analysis_status[session_id] = {'status': 'starting', 'progress': 0}
    
    run_security_analysis(session_id, )

    # thread = threading.Thread(target=run_security_analysis, args=(session_id,))
    # thread.daemon = True
    # thread.start()
    
    return jsonify({'message': 'Analysis started', 'session_id': session_id})

@app.route('/status/<session_id>')
def get_status(session_id):
    status = analysis_status.get(session_id, {'status': 'not_found'})
    return jsonify(status)

@app.route('/download/<session_id>')
def download_report(session_id):
    pdf_path = os.path.join(app.config['REPORTS_FOLDER'], f'pentest_report_{session_id}.pdf')
    
    if not os.path.exists(pdf_path):
        return jsonify({'error': 'Report not found'}), 404
    
    return send_file(pdf_path, as_attachment=True, download_name=f'pentest_report_{datetime.now().strftime("%Y%m%d_%H%M%S")}.pdf')

@app.route('/results/<session_id>')
def show_results(session_id):
    status = analysis_status.get(session_id, {'status': 'not_found'})
    return render_template('results.html', session_id=session_id, status=status)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)