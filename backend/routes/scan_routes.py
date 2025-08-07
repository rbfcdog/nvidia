# backend/routes/scan_routes.py
import json
import uuid
from typing import List
from fastapi import APIRouter, HTTPException, File, UploadFile
from backend.services.rabbitmq_service import RabbitMQService
from backend.services.scan_service import ScanService

scan_router = APIRouter()

# ROTA ANTIGA - MANTIDA PARA REFERÊNCIA
@scan_router.post("/upload", status_code=202)
async def upload_files_for_analysis(files: List[UploadFile] = File(...)):
    # ... (código original inalterado) ...
    scan_id = uuid.uuid4().hex
    service = ScanService()
    try:
        saved_files = await service.save_text_files(files, scan_id)
        rabbitmq = RabbitMQService()
        message_payload = {"scan_id": scan_id}
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

# ===================================================================
# ===== NOVA ROTA ADICIONADA PARA COMPILAR OS ARQUIVOS TXT =========
# ===================================================================
@scan_router.post("/compile-texts", status_code=200)
async def compile_text_files(files: List[UploadFile] = File(...)):
    """
    Recebe múltiplos arquivos .txt e os compila em um único arquivo.
    """
    # Gera um nome de arquivo único para o compilado.
    # Pode ser um UUID, um timestamp, ou baseado em um ID de análise.
    compiled_filename = f"compilado_{uuid.uuid4().hex[:8]}.txt"
    service = ScanService()

    try:
        # Chama a nova função de serviço para compilar os arquivos
        compiled_file_path = await service.compile_text_files(files, compiled_filename)

        # Retorna uma resposta de sucesso para o frontend
        return {
            "message": f"{len(files)} arquivos foram compilados com sucesso.",
            "compiled_file": str(compiled_file_path.name) # Retorna apenas o nome do arquivo gerado
        }
    except ValueError as e:
        # Erro de validação (ex: arquivo não-txt)
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        # Outros erros inesperados
        print(f"Erro inesperado durante a compilação: {e}")
        raise HTTPException(status_code=500, detail="Ocorreu um erro interno ao compilar os arquivos.")