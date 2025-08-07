# backend/services/scan_service.py
import json
import markdown2
import shutil
from pathlib import Path
from typing import List
from fastapi import UploadFile
import weasyprint

# Use caminhos relativos ao arquivo atual para robustez
BASE_DIR = Path(__file__).resolve().parent.parent
# ===== NOVO DIRETÓRIO DE DESTINO PARA O ARQUIVO COMPILADO =====
USERFILES_DIR = BASE_DIR.parent / "userfiles"
# Diretórios antigos mantidos para as outras funções
SUBMISSIONS_DIR = BASE_DIR.parent / "submissions"
REPORTS_DIR = BASE_DIR.parent / "reports"

class ScanService:
    """
    Lida com o upload de arquivos de texto, compilação, conversão de relatórios e status.
    """
    def __init__(self):
        # Garante que os diretórios existam
        SUBMISSIONS_DIR.mkdir(exist_ok=True)
        REPORTS_DIR.mkdir(exist_ok=True)
        # ===== GARANTE QUE O NOVO DIRETÓRIO EXISTA =====
        USERFILES_DIR.mkdir(exist_ok=True)

    # ===================================================================
    # ===== NOVA FUNÇÃO ADICIONADA PARA COMPILAR OS ARQUIVOS TXT ======
    # ===================================================================
    async def compile_text_files(self, files: List[UploadFile], output_filename: str) -> Path:
        """
        Recebe uma lista de arquivos de upload, valida se são .txt,
        e compila o conteúdo de todos em um único arquivo de texto.
        """
        compiled_content = []

        for file in files:
            # 1. Validação: Checa se o arquivo é um .txt
            if not file.filename.endswith(".txt"):
                raise ValueError(f"Arquivo inválido: {file.filename}. Apenas arquivos .txt são permitidos.")
            
            # 2. Lê o conteúdo do arquivo
            # Usamos await file.read() pois é uma operação assíncrona
            content_bytes = await file.read()
            
            # 3. Adiciona um cabeçalho para identificar o arquivo original
            compiled_content.append(f"--- INÍCIO DO ARQUIVO: {file.filename} ---\n")
            compiled_content.append(content_bytes.decode('utf-8'))
            compiled_content.append("\n--- FIM DO ARQUIVO ---\n\n")

        # 4. Define o caminho final do arquivo compilado
        output_path = USERFILES_DIR / output_filename

        # 5. Escreve o conteúdo compilado no novo arquivo
        with open(output_path, "w", encoding="utf-8") as f:
            f.write("".join(compiled_content))
            
        return output_path

    # Funções originais mantidas sem alterações
    async def save_text_files(self, files: List[UploadFile], scan_id: str) -> List[Path]:
        # ... (código original inalterado) ...
        scan_submission_dir = SUBMISSIONS_DIR / scan_id
        scan_submission_dir.mkdir(exist_ok=True)
        saved_files_paths = []
        for file in files:
            if not file.filename.endswith(".txt"):
                shutil.rmtree(scan_submission_dir)
                raise ValueError(f"Arquivo inválido: {file.filename}. Apenas arquivos .txt são permitidos.")
            file_path = scan_submission_dir / file.filename
            with open(file_path, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
            saved_files_paths.append(file_path)
        return saved_files_paths

    def convert_md_to_pdf(self, scan_id: str) -> Path:
        # ... (código original inalterado) ...
        md_report_path = REPORTS_DIR / f"{scan_id}.md"
        pdf_report_path = REPORTS_DIR / f"{scan_id}.pdf"
        if not md_report_path.exists():
            raise FileNotFoundError("Relatório em Markdown não encontrado.")
        with open(md_report_path, 'r', encoding='utf-8') as f:
            md_content = f.read()
        html_content = markdown2.markdown(md_content, extras=["fenced-code-blocks", "tables"])
        html_with_style = f"""
        <html>...</html>
        """
        weasyprint.HTML(string=html_with_style).write_pdf(pdf_report_path)
        return pdf_report_path
        
    def get_report_status(self, scan_id: str) -> dict:
        # ... (código original inalterado) ...
        md_report_path = REPORTS_DIR / f"{scan_id}.md"
        submission_dir = SUBMISSIONS_DIR / scan_id
        if md_report_path.exists():
            return {"scan_id": scan_id, "status": "Concluído"}
        if submission_dir.exists():
            return {"scan_id": scan_id, "status": "Em Andamento"}
        return {"scan_id": scan_id, "status": "Não Encontrado"}