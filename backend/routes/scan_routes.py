# backend/routes/scan_routes.py
from fastapi import APIRouter, HTTPException
from backend.services.rabbitmq_service import RabbitMQService
from backend.services.scan_service import ScanService
from backend.schemas.submission import SubmissionRequest, SubmissionResponse, Submission
from typing import List
import uuid
from pathlib import Path
import json

scan_router = APIRouter()
SUBMISSIONS_DIR = Path("./submissions")

@scan_router.post("/submit-form", response_model=SubmissionResponse, status_code=202)
async def submit_form(request: SubmissionRequest):
    """
    Recebe os dados do formulário, salva e envia para a fila de análise.
    """
    scan_id = uuid.uuid4().hex
    
    # Prepara os dados para salvar e para a fila
    submission_data = request.dict(by_alias=True) # Usa os aliases definidos no schema
    message_payload = {
        "scan_id": scan_id,
        "data": submission_data
    }

    try:
        # 1. Salva os dados da submissão em um arquivo local
        SUBMISSIONS_DIR.mkdir(exist_ok=True)
        submission_path = SUBMISSIONS_DIR / f"{scan_id}.json"
        with open(submission_path, "w") as f:
            json.dump(submission_data, f, indent=2)
        
        # 2. Envia a mensagem para os agentes de IA via RabbitMQ
        rabbitmq = RabbitMQService()
        rabbitmq.send_message(
            queue_name="ai_scan_queue", # Fila dedicada para os agentes
            message=json.dumps(message_payload)
        )
        
        return SubmissionResponse(scan_id=scan_id)
    except Exception as e:
        # Em caso de falha, é importante logar o erro
        print(f"Erro ao submeter formulário: {e}")
        raise HTTPException(status_code=500, detail="Ocorreu um erro interno ao processar sua solicitação.")

@scan_router.get("/submissions", response_model=List[Submission])
async def get_all_submissions():
    """
    Retorna uma lista de todas as análises que já foram submetidas.
    """
    service = ScanService()
    return service.get_all_submissions()