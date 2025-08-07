# backend/services/scan_service.py
import json
from pathlib import Path
from typing import List, Optional, Dict, Any

# Define os diretórios como constantes para fácil manutenção
SUBMISSIONS_DIR = Path("./submissions")
REPORTS_DIR = Path("./reports")

class ScanService:
    """
    Contém a lógica de negócio para manipular submissões e relatórios.
    """

    def get_all_submissions(self) -> List[Dict[str, Any]]:
        """Lista todas as submissões já realizadas."""
        SUBMISSIONS_DIR.mkdir(exist_ok=True)
        submissions = []
        for file_path in SUBMISSIONS_DIR.glob("*.json"):
            with open(file_path, "r") as f:
                data = json.load(f)
                # Adiciona o scan_id que é o nome do arquivo sem a extensão
                submission_info = {
                    "scan_id": file_path.stem,
                    "data": data
                }
                submissions.append(submission_info)
        return submissions

    def check_report_status(self, scan_id: str) -> Dict[str, str]:
        """Verifica o status de uma análise."""
        report_path = REPORTS_DIR / f"{scan_id}.json"
        submission_path = SUBMISSIONS_DIR / f"{scan_id}.json"

        if report_path.exists():
            return {"scan_id": scan_id, "status": "Concluído"}
        
        if submission_path.exists():
            return {"scan_id": scan_id, "status": "Em Andamento"}
        
        return {"scan_id": scan_id, "status": "Não Encontrado"}

    def get_report(self, scan_id: str) -> Optional[Dict[str, Any]]:
        """Busca o relatório final de uma análise."""
        REPORTS_DIR.mkdir(exist_ok=True)
        report_path = REPORTS_DIR / f"{scan_id}.json"
        if not report_path.exists():
            return None
        with open(report_path, "r") as f:
            return json.load(f)