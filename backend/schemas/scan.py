from pydantic import BaseModel

class ScanRequest(BaseModel):
    target: str
    scan_type: str  # "ssh" ou "web"

class ScanResponse(BaseModel):
    scan_id: str
    status: str

class SubmissionRequest(BaseModel):
    employee_name: str
    company_name: str
    cnpj: str
    ip: str
    url: str
