import json
import markdown2
import shutil
from pathlib import Path
from typing import List
from fastapi import UploadFile
import weasyprint

# Use caminhos relativos ao arquivo atual para robustez
BASE_DIR = Path(__file__).resolve().parent.parent
SUBMISSIONS_DIR = BASE_DIR.parent / "submissions"
REPORTS_DIR = BASE_DIR.parent / "reports"

class ScanService:
    """
    Lida com o upload de arquivos de texto, conversão de relatórios e status.
    """
    def __init__(self):
        # Garante que os diretórios existam
        SUBMISSIONS_DIR.mkdir(exist_ok=True)
        REPORTS_DIR.mkdir(exist_ok=True)

    async def save_text_files(self, files: List[UploadFile], scan_id: str) -> List[Path]:
        """
        Valida e salva múltiplos arquivos .txt em uma pasta de submissão.
        Retorna uma lista com os caminhos dos arquivos salvos.
        """
        scan_submission_dir = SUBMISSIONS_DIR / scan_id
        scan_submission_dir.mkdir(exist_ok=True)
        saved_files_paths = []

        for file in files:
            # 1. Validação: Checa se o arquivo é um .txt
            if not file.filename.endswith(".txt"):
                # Limpa a pasta se um arquivo for inválido
                shutil.rmtree(scan_submission_dir)
                raise ValueError(f"Arquivo inválido: {file.filename}. Apenas arquivos .txt são permitidos.")
            
            file_path = scan_submission_dir / file.filename
            
            # 2. Salva o arquivo
            with open(file_path, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
            
            saved_files_paths.append(file_path)
            
        return saved_files_paths

    def convert_md_to_pdf(self, scan_id: str) -> Path:
        """
        Converte um relatório .md para .pdf.
        Retorna o caminho do arquivo PDF gerado.
        """
        md_report_path = REPORTS_DIR / f"{scan_id}.md"
        pdf_report_path = REPORTS_DIR / f"{scan_id}.pdf"

        if not md_report_path.exists():
            raise FileNotFoundError("Relatório em Markdown não encontrado.")
            
        # Lê o conteúdo do Markdown
        with open(md_report_path, 'r', encoding='utf-8') as f:
            md_content = f.read()

        # Converte Markdown para HTML
        html_content = markdown2.markdown(md_content, extras=["fenced-code-blocks", "tables"])
        
        # Adiciona um estilo básico para o PDF ficar mais legível
        html_with_style = f"""
        <html>
            <head>
                <style>
                    body {{ font-family: sans-serif; line-height: 1.6; }}
                    code {{ background-color: #f4f4f4; padding: 2px 4px; border-radius: 4px; font-family: monospace; }}
                    pre {{ background-color: #f4f4f4; padding: 1rem; border-radius: 4px; white-space: pre-wrap; }}
                    table {{ border-collapse: collapse; width: 100%; }}
                    th, td {{ border: 1px solid #ddd; padding: 8px; }}
                    th {{ background-color: #f2f2f2; }}
                </style>
            </head>
            <body>
                {html_content}
            </body>
        </html>
        """

        # Converte HTML para PDF
        weasyprint.HTML(string=html_with_style).write_pdf(pdf_report_path)
        
        return pdf_report_path
        
    def get_report_status(self, scan_id: str) -> dict:
        """
        Verifica o status da análise. Agora checa pela existência do relatório .md
        """
        md_report_path = REPORTS_DIR / f"{scan_id}.md"
        submission_dir = SUBMISSIONS_DIR / scan_id

        if md_report_path.exists():
            return {"scan_id": scan_id, "status": "Concluído"}
        
        if submission_dir.exists():
            return {"scan_id": scan_id, "status": "Em Andamento"}
        
        return {"scan_id": scan_id, "status": "Não Encontrado"}