from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes.scan_routes import scan_router
from backend.routes.report_routes import report_router
import os
from pathlib import Path

app = FastAPI(title="Sistema de Segurança com Agentes de IA")

# --- CONFIGURAÇÃO DO CORS ---
# Lista de origens que podem fazer requisições para a API.
# Para desenvolvimento, liberamos o servidor do Next.js.
origins = [
    "http://localhost:3000", # Endereço padrão do Next.js
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # Permite todos os métodos (GET, POST, etc.)
    allow_headers=["*"], # Permite todos os cabeçalhos
)
# --- FIM DA CONFIGURAÇÃO DO CORS ---

@app.on_event("startup")
async def startup_event():
    # Cria diretórios se não existirem
    Path("./reports").mkdir(exist_ok=True)
    Path("./submissions").mkdir(exist_ok=True)
    print(f"Server rodando em http://localhost:{os.getenv('FASTAPI_PORT')}")

app.include_router(scan_router, prefix="/api/v1", tags=["scans"])
app.include_router(report_router, prefix="/api/v1", tags=["reports"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("FASTAPI_PORT")))
