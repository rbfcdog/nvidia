# backend/routes/scan_routes.py
import json
import uuid
from typing import List
from fastapi import APIRouter, HTTPException, File, UploadFile
from backend.services.rabbitmq_service import RabbitMQService
from backend.services.scan_service import ScanService

scan_router = APIRouter()

@scan_router.post("/upload", status_code=202) # Rota simplificada
async def upload_files_for_analysis(files: List[UploadFile] = File(...)):
    scan_id = uuid.uuid4().hex
    service = ScanService()

    try:
        saved_files = await service.save_text_files(files, scan_id)

        rabbitmq = RabbitMQService()
        message_payload = {"scan_id": scan_id} # Agente só precisa do ID para achar a pasta
        rabbitmq.send_message(
            queue_name="ai_scan_queue",
            message=json.dumps(message_payload)
        )

        return {"scan_id": scan_id, "message": f"{len(files)} arquivos recebidos. Análise iniciada."}

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        print(f"Erro inesperado no upload: {e}")
        raise HTTPException(status_code=500, detail="Ocorreu um erro interno ao processar os arquivos.")