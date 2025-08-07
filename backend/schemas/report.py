# backend/schemas/report.py
from pydantic import BaseModel, Field
from typing import List, Literal

# Sub-modelo para uma única vulnerabilidade encontrada
class Vulnerability(BaseModel):
    scan_type: str = Field(..., description="Tipo de teste que encontrou a falha (ex: SQL Injection, XSS)")
    severity: Literal['Crítica', 'Alta', 'Média', 'Baixa', 'Informativa']
    description: str = Field(..., description="Descrição técnica da vulnerabilidade")
    recommendation: str = Field(..., description="Sugestão para corrigir a falha")

# Modelo para o status da análise
class StatusResponse(BaseModel):
    scan_id: str
    status: Literal['Pendente', 'Em Andamento', 'Concluído', 'Não Encontrado']

# Modelo principal do relatório final que será gerado pelos agentes de IA
class Report(BaseModel):
    scan_id: str
    company_name: str
    target_ip: str
    target_url: str
    status: Literal['Concluído'] = 'Concluído'
    summary: str = Field(..., description="Resumo executivo da análise de segurança")
    vulnerabilities: List[Vulnerability] = []