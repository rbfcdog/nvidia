from pathlib import Path
from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse, JSONResponse
from backend.services.scan_service import ScanService

report_router = APIRouter()

@report_router.get("/status/{scan_id}")
async def check_status(scan_id: str):
    """
    Verifica e retorna o status atual de uma análise.
    """
    service = ScanService()
    status_info = service.get_report_status(scan_id)
    if status_info["status"] == "Não Encontrado":
        raise HTTPException(status_code=404, detail="Análise com o ID fornecido não encontrada.")
    return JSONResponse(content=status_info)

@report_router.get("/report/{scan_id}/download")
async def download_report_pdf(scan_id: str):
    """
    Converte o relatório .md para .pdf (se necessário) e o disponibiliza para download.
    """
    service = ScanService()
    pdf_report_path = Path(service.REPORTS_DIR) / f"{scan_id}.pdf"
    md_report_path = Path(service.REPORTS_DIR) / f"{scan_id}.md"

    try:
        # Se o PDF não existir mas o MD sim, converte-o
        if not pdf_report_path.exists() and md_report_path.exists():
            service.convert_md_to_pdf(scan_id)
        
        # Se o PDF (agora) existir, envia-o
        if pdf_report_path.exists():
            return FileResponse(
                path=pdf_report_path,
                filename=f"relatorio_seguranca_{scan_id}.pdf",
                media_type='application/pdf'
            )
        else:
             # Se nem o MD existir, o relatório não está pronto
            raise FileNotFoundError
            
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Relatório ainda não está pronto ou não foi encontrado.")
    except Exception as e:
        print(f"Erro ao gerar/enviar PDF: {e}")
        raise HTTPException(status_code=500, detail="Não foi possível gerar ou baixar o relatório em PDF.")