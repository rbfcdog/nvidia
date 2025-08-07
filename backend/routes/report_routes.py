# backend/routes/report_routes.py
from fastapi import APIRouter, HTTPException
from backend.services.scan_service import ScanService
from backend.schemas.report import Report, StatusResponse

report_router = APIRouter()

@report_router.get("/status/{scan_id}", response_model=StatusResponse)
async def check_status(scan_id: str):
    """
    Verifica e retorna o status atual de uma análise: 
    Pendente, Em Andamento, ou Concluído.
    """
    service = ScanService()
    status_info = service.check_report_status(scan_id)
    if status_info["status"] == "Não Encontrado":
        raise HTTPException(status_code=404, detail="Análise com o ID fornecido não encontrada.")
    return status_info

@report_router.get("/report/{scan_id}", response_model=Report)
async def get_report(scan_id: str):
    """
    Retorna o relatório de segurança detalhado de uma análise concluída.
    """
    service = ScanService()
    report = service.get_report(scan_id)
    if not report:
        raise HTTPException(status_code=404, detail="Relatório não encontrado. A análise pode não existir ou não ter sido concluída.")
    return report