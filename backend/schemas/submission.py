# backend/schemas/submission.py
from pydantic import BaseModel, Field
import uuid

# Modelo para os dados recebidos do formulário do frontend
class SubmissionRequest(BaseModel):
    employee_name: str = Field(..., description="Nome do funcionário solicitante")
    company_name: str = Field(..., description="Nome da empresa")
    cnpj: str = Field(..., description="CNPJ da empresa (somente números)")
    ip: str = Field(..., alias="targetIP", description="Endereço IP do alvo")
    url: str = Field(..., alias="systemURL", description="URL do sistema web")

    class Config:
        populate_by_name = True # Permite usar 'targetIP' e 'systemURL' do JSON do front

# Modelo para a resposta ao criar uma nova submissão
class SubmissionResponse(BaseModel):
    scan_id: str = Field(..., description="ID único para rastreamento da análise")
    message: str = "Análise iniciada. Acompanhe o status usando o scan_id."

# Modelo para representar uma submissão salva
class Submission(BaseModel):
    scan_id: str
    data: SubmissionRequest