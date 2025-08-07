from crewai import Agent
from llm_config import get_nvidia_llm

# Get the configured LLM
llm = get_nvidia_llm()

analizador_agent = Agent(
    role="Analisador de Relatórios de Segurança",
    goal="Extrair e estruturar vulnerabilidades de relatórios brutos em JSON padronizado para análise especializada.",
    backstory=(
        "Especialista em parsing de outputs de ferramentas de segurança (Nmap, Nessus, etc). "
        "Foco: extrair dados técnicos precisos e classificar por categoria sem interpretação profunda."
    ),
    llm=llm,
    verbose=False,
    allow_delegation=False,  # Reduzir overhead de delegação
    max_iter=2,  # Limitar iterações
    max_execution_time=180,  # 3 minutos máximo
    tools=[]
)

especialista_rede = Agent(
    role="Especialista em Segurança de Rede",
    goal="Analisar vulnerabilidades de rede e propor soluções técnicas específicas.",
    backstory=(
        "Engenheiro de redes com foco em hardening de protocolos TCP/IP, SSH, FTP, SMB. "
        "Análise direta: risco + solução técnica concreta."
    ),
    llm=llm,
    verbose=False,
    allow_delegation=False,
    max_iter=1,  # Reduzido para 1 iteração
    max_execution_time=120,  # 2 minutos máximo
    tools=[]
)

especialista_web = Agent(
    role="Especialista em Segurança Web",
    goal="Analisar falhas web conforme OWASP Top 10 e fornecer correções práticas.",
    backstory=(
        "Desenvolvedor/hacker ético especializado em AppSec. "
        "Foco: SQLi, XSS, CSRF, misconfigurations. Soluções práticas no código."
    ),
    llm=llm,
    verbose=False,
    allow_delegation=False,
    max_iter=1,  # Reduzido para 1 iteração
    max_execution_time=120,  # 2 minutos máximo
    tools=[]
)

especialista_infra = Agent(
    role="Especialista em Infraestrutura",
    goal="Avaliar configurações de sistemas e propor hardening baseado em best practices.",
    backstory=(
        "SysAdmin focado em segurança de SO, patches, permissões e serviços. "
        "Expertise em CIS Benchmarks e hardening guides."
    ),
    llm=llm,
    verbose=False,
    allow_delegation=False,
    max_iter=1,  # Reduzido para 1 iteração
    max_execution_time=120,  # 2 minutos máximo
    tools=[]
)

redator_executivo = Agent(
    role="Redator de Relatórios de Segurança",
    goal="Sintetizar análises técnicas em relatório executivo claro e priorizado.",
    backstory=(
        "Consultor sênior especializado em comunicação técnica. "
        "Traduz análises complexas em planos de ação executáveis para técnicos e gestores."
    ),
    llm=llm,
    verbose=False,  # Reduzido para False
    allow_delegation=False,
    max_iter=1,  # Reduzido para 1 iteração
    max_execution_time=180,  # 3 minutos máximo
    tools=[]
)