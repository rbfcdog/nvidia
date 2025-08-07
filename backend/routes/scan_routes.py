from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from backend.services.rabbitmq_service import RabbitMQService
from backend.schemas.scan import ScanRequest, SubmissionRequest
import uuid
from pathlib import Path
import json

scan_router = APIRouter()

class ScanRequest(BaseModel):
    target: str  # IP ou URL alvo
    scan_type: str  # "ssh" ou "web"

@scan_router.post("/scan")
async def start_scan(request: ScanRequest):
    try:
        rabbitmq = RabbitMQService()
        await rabbitmq.send_message(
            queue_name=f"{request.scan_type}_scan_queue",
            message=request.json()
        )
        return {"message": f"Varredura {request.scan_type} iniciada"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
