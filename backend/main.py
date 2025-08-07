from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes.scan_routes import scan_router
from backend.routes.report_routes import report_router
import os
from pathlib import Path
import uvicorn # Importado aqui para uso no __main__

# Cria a aplicação FastAPI
app = FastAPI(
    title="CyberOps Copilot API",
    description="API para orquestrar análises de segurança com agentes de IA.",
    version="1.0.0"
)

# --- CONFIGURAÇÃO DO CORS ---
# Define quais origens (frontends) podem fazer requisições para esta API.
# Essencial para que seu Next.js (rodando em localhost:3000) possa se comunicar com o FastAPI.
origins = [
    "http://localhost:3000", # Endereço padrão do Next.js em desenvolvimento
    # Em produção, você adicionaria o domínio do seu site aqui.
    # Ex: "https://www.meuprojeto.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # Permite todos os métodos (GET, POST, etc.)
    allow_headers=["*"], # Permite todos os cabeçalhos
)
# --- FIM DA CONFIGURAÇÃO DO CORS ---


# --- EVENTO DE INICIALIZAÇÃO ---
@app.on_event("startup")
async def startup_event():
    """
    Esta função é executada uma vez, quando o servidor FastAPI inicia.
    É o lugar perfeito para criar os diretórios necessários para o projeto.
    """
    # Garante que os diretórios para relatórios, submissões e arquivos de usuário existam.
    Path("./reports").mkdir(exist_ok=True)
    Path("./submissions").mkdir(exist_ok=True)
    Path("./userfiles").mkdir(exist_ok=True) # <-- ADICIONADO: Cria a pasta para os arquivos compilados
    print("Diretórios necessários verificados/criados com sucesso.")
    # A porta é lida do ambiente, mas o uvicorn.run define onde o servidor realmente roda.
    print(f"Servidor FastAPI iniciado. Acesse a documentação em http://localhost:8000/docs")


# --- REGISTRO DOS ROTEADORES ---
# Aqui, conectamos os arquivos de rotas à aplicação principal.
# Usamos prefixos para organizar as URLs da API de forma lógica.

# Todas as rotas definidas em 'scan_router' (de scan_routes.py)
# estarão sob o prefixo /api/v1/scan
# Exemplo: /api/v1/scan/compile-texts
app.include_router(scan_router, prefix="/api/v1/scan", tags=["Análises (Scans)"])

# Todas as rotas definidas em 'report_router' (de report_routes.py)
# estarão sob o prefixo /api/v1/report
# Exemplo: /api/v1/report/status/{scan_id}
app.include_router(report_router, prefix="/api/v1/report", tags=["Relatórios (Reports)"])


# --- PONTO DE ENTRADA PARA EXECUTAR O SERVIDOR ---
# Este bloco permite que você rode o servidor diretamente com o comando: python main.py
if __name__ == "__main__":
    # Carrega a porta a partir de uma variável de ambiente, com 8000 como padrão.
    # É uma boa prática não deixar valores fixos no código.
    port = int(os.getenv("FASTAPI_PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
