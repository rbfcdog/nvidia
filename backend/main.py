from fastapi import FastAPI
from backend.routes.scan_routes import scan_router
from backend.routes.report_routes import report_router
import os

app = FastAPI(title="Sistema de Segurança com Agentes de IA")
app.include_router(scan_router, prefix="/api/v1", tags=["scans"])
app.include_router(report_router, prefix="/api/v1", tags=["reports"])

@app.on_event("startup")
async def startup_event():
    print(f"Server rodando em http://localhost:{os.getenv('FASTAPI_PORT')}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("FASTAPI_PORT")))
