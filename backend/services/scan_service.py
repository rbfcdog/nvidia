import os
import json
from pathlib import Path

REPORTS_DIR = Path("./reports")

class ScanService:
    async def get_report(self, scan_id: str):
        report_path = REPORTS_DIR / f"{scan_id}.json"
        if not report_path.exists():
            return None
        with open(report_path, "r") as f:
            return json.load(f)
