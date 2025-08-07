from crewai import Task
from agent import *

task_estruturar_relatorio = Task(
    description="""
    OBJETIVO ESPECÍFICO: Processar o arquivo input/recon_raw_output.txt e extrair dados estruturados.
    
    INSTRUÇÕES DIRETAS:
    1. Leia o arquivo e extraia:
       - IPs/domínios alvo
       - Portas abertas + serviços + versões
       - Scripts NSE executados
       - Indicadores de vulnerabilidade
    
    2. Para cada achado, crie um objeto JSON:
    {
      "id": [número],
      "type": "network|web|infrastructure|system",
      "port": [porta],
      "service": "[serviço]",
      "version": "[versão]",
      "finding": "[descrição concisa]",
      "evidence": "[evidência do scan]",
      "risk_severity_hint": "critical|high|medium|low"
    }
    
    3. Classifique por tipo:
       - network: SSH, FTP, SMB, Telnet, SNMP
       - web: HTTP/HTTPS, aplicações web
       - infrastructure: DNS, configurações de rede
       - system: OS, serviços locais
    
    SAÍDA: Array JSON válido em outputs/structured_analysis.json
    NÃO INTERPRETE - APENAS EXTRAIA E ESTRUTURE.
    """,
    expected_output="JSON estruturado com lista de vulnerabilidades classificadas e evidências extraídas do scan.",
    agent=analizador_agent,
    input_file="input/recon_raw_output.txt",
    output_file="outputs/structured_analysis.json"
)

task_rede = Task(
    description="""
    ANÁLISE FOCADA: Processar APENAS achados type="network" do structured_analysis.json.
    
    Para cada vulnerabilidade de rede:
    1. Risco: Critical/High/Medium/Low + justificativa técnica
    2. Vetor de ataque: Como explorar (ex: brute force SSH port 22)
    3. Impacto: Consequências específicas (ex: shell remoto, lateral movement)
    4. Mitigação: Comandos/configurações exatas
       - Ex: "Desabilitar root login: echo 'PermitRootLogin no' >> /etc/ssh/sshd_config"
    
    FORMATO: Markdown conciso, máximo 800 palavras.
    FOCO: Soluções práticas imediatas.
    """,
    expected_output="Relatório Markdown com análise de vulnerabilidades de rede, riscos e comandos de correção.",
    agent=especialista_rede,
    input_file="outputs/structured_analysis.json",
    output_file="outputs/report_sections/network_findings.md"
)

task_web = Task(
    description="""
    ANÁLISE FOCADA: Processar APENAS achados type="web" do structured_analysis.json.
    
    Para cada vulnerabilidade web:
    1. Classificação OWASP Top 10 (ex: A03:2021 - Injection)
    2. Scenario de exploração específico
    3. Impacto técnico direto
    4. Correção prática:
       - Código seguro quando aplicável
       - Headers de segurança
       - Configurações de servidor
    
    FORMATO: Markdown conciso, máximo 800 palavras.
    FOCO: Soluções implementáveis imediatamente.
    """,
    expected_output="Relatório Markdown com falhas web, classificação OWASP e correções técnicas específicas.",
    agent=especialista_web,
    input_file="outputs/structured_analysis.json",
    output_file="outputs/report_sections/web_findings.md"
)

task_infra = Task(
    description="""
    ANÁLISE FOCADA: Processar APENAS achados type="infrastructure" e "system" do structured_analysis.json.
    
    Para cada vulnerabilidade de infraestrutura:
    1. Componente afetado (OS, serviço, configuração)
    2. Risco de negócio direto
    3. Plano de correção imediato:
       - Comandos de patch específicos
       - Configurações de hardening
       - Desativação de serviços desnecessários
    
    FORMATO: Markdown conciso, máximo 800 palavras.
    REFERÊNCIA: CIS Benchmarks quando aplicável.
    """,
    expected_output="Relatório Markdown com falhas de infraestrutura e plano de hardening específico.",
    agent=especialista_infra,
    input_file="outputs/structured_analysis.json",
    output_file="outputs/report_sections/infra_findings.md"
)

task_relatorio_final = Task(
    description="""
    COMPILAÇÃO FINAL: Ler os 3 arquivos de análise e criar relatório executivo.
    
    ESTRUTURA OBRIGATÓRIA:
    # Relatório de Teste de Invasão
    
    ## Sumário Executivo
    - Total de vulnerabilidades por criticidade
    - 3 riscos principais
    - Recomendação de prioridade
    
    ## Vulnerabilidades por Criticidade
    ### 🔴 Crítico
    ### 🟠 Alto  
    ### 🟡 Médio
    ### 🔵 Baixo
    
    Para cada: Título | Categoria | Impacto | Ação Corretiva
    
    ## Próximos Passos
    - Ordem de correção recomendada
    - Timeline sugerido
    - Recomendações contínuas
    
    LINGUAGEM: Técnica mas acessível para gestores.
    TAMANHO: Máximo 1500 palavras.
    """,
    expected_output="Relatório executivo completo em Markdown, estruturado e pronto para entrega.",
    agent=redator_executivo,
    input_file=["outputs/report_sections/network_findings.md", "outputs/report_sections/web_findings.md", "outputs/report_sections/infra_findings.md"],
    output_file="outputs/pentest_report.md"
)