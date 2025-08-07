from fastapi import APIRouter
from fastapi.responses import JSONResponse
from backend.services.scan_service import ScanService

report_router = APIRouter()

@report_router.get("/report/{scan_id}")
async def get_report(scan_id: str):
    service = ScanService()
    report = await service.get_report(scan_id)
    if not report:
        return JSONResponse(status_code=404, content={"error": "Relatório não encontrado"})
    return JSONResponse(content=report)
