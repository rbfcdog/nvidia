# Projeto CrewAI com Múltiplos Agentes

Este projeto demonstra como usar o CrewAI para criar e coordenar múltiplos agentes de IA usando a API da NVIDIA para inferência de modelos de linguagem.

-----

## Estrutura do Projeto

```
nvidia/
├── .env # Variáveis de ambiente (chaves de API)
├── llm_config.py # Configuração LLM para a API NVIDIA
├── agents.py # Definições dos agentes
├── tasks.py # Definições das tarefas
├── crew_main.py # Fluxo de trabalho principal da equipe (crew)
├── examples.py # Implementações de exemplo
├── allan/
│ └── chamada_api.py # Exemplo original de chamada de API NVIDIA
└── README.md # Este arquivo
```

-----

## Funcionalidades

### Múltiplos Tipos de Agentes

1.  **Agente de Pesquisa**: Conduz pesquisas aprofundadas e coleta informações.
2.  **Agente Criador de Conteúdo**: Cria conteúdo envolvente com base na pesquisa.
3.  **Agente de Garantia de Qualidade**: Revisa e aprimora a qualidade do conteúdo.
4.  **Agente Gerente de Projeto**: Coordena o fluxo de trabalho e gerencia o projeto.

### Capacidades Chave

  - **Fluxo de Trabalho Sequencial**: As tarefas são executadas em ordem lógica com dependências.
  - **Compartilhamento de Contexto**: Agentes podem acessar saídas de tarefas anteriores.
  - **Integração com a API NVIDIA**: Usa o modelo Llama da NVIDIA através de sua API.
  - **Criação Flexível de Tarefas**: Fácil de criar novas tarefas e fluxos de trabalho.
  - **Registro Detalhado**: Saída abrangente para monitoramento do progresso.

-----

## Instruções de Configuração

### 1\. Configuração do Ambiente

Certifique-se de ter o Python 3.8+ instalado e, em seguida, instale as dependências:

```bash
pip install crewai langchain langchain-openai python-dotenv
```

### 2\. Configuração da API

O projeto já está configurado para usar sua chave de API NVIDIA. A configuração está em `.env`:

```
NVIDIA_API_KEY=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
NVIDIA_BASE_URL=https://integrate.api.nvidia.com/v1
```

### 3\. Executando o Projeto

#### Exemplo de Fluxo de Trabalho Completo

```bash
python crew_main.py
```

Digite um tópico quando solicitado e observe como os quatro agentes colaboram para pesquisar, criar conteúdo, revisá-lo e gerenciar o projeto.

#### Exemplos Simples

```bash
python examples.py
```

Escolha entre diferentes cenários de exemplo:

  - Equipe simples com 2 agentes
  - Múltiplas tarefas de pesquisa
  - Fluxo de trabalho completo

#### Componentes Individuais

```bash
# Testar apenas os agentes
python -c "from agents import *; print('Agentes carregados com sucesso!')"

# Testar a configuração do LLM
python -c "from llm_config import get_nvidia_llm; llm = get_nvidia_llm(); print('LLM configurado!')"
```

-----

## Exemplos de Uso

### Uso Básico

```python
from crew_main import run_content_creation_project

# Executar um fluxo de trabalho completo de criação de conteúdo
result = run_content_creation_project("Inteligência Artificial na Saúde")
```

### Criação de Equipe Personalizada

```python
from crewai import Crew, Process
from agents import research_agent, content_creator_agent
from tasks import create_research_task, create_content_creation_task

# Criar fluxo de trabalho personalizado
topic = "Seu Tópico Aqui"
research_task = create_research_task(topic)
content_task = create_content_creation_task(topic)

content_task.context = [research_task]

crew = Crew(
    agents=[research_agent, content_creator_agent],
    tasks=[research_task, content_task],
    process=Process.sequential
)

result = crew.kickoff()
```

-----

## Papéis e Responsabilidades dos Agentes

### 🔍 Agente de Pesquisa

  - Coleta informações abrangentes
  - Identifica conceitos e tendências chave
  - Encontra fontes e estatísticas credíveis
  - Analisa desenvolvimentos atuais

### ✍️ Agente Criador de Conteúdo

  - Transforma a pesquisa em conteúdo envolvente
  - Estrutura as informações de forma eficaz
  - Cria narrativas convincentes
  - Otimiza para legibilidade

### 🔍 Agente de Garantia de Qualidade

  - Revisa o conteúdo para precisão
  - Verifica gramática e estilo
  - Garante coerência e fluidez
  - Fornece sugestões de melhoria

### 📋 Agente Gerente de Projeto

  - Coordena as atividades da equipe
  - Monitora o progresso e os prazos
  - Garante que os objetivos sejam atingidos
  - Fornece resumos do projeto

-----

## Processo do Fluxo de Trabalho

1.  **Fase de Pesquisa**: O agente de pesquisa coleta informações abrangentes.
2.  **Criação de Conteúdo**: O criador de conteúdo transforma a pesquisa em conteúdo envolvente.
3.  **Revisão de Qualidade**: O agente de QA revisa e aprimora o conteúdo.
4.  **Gerenciamento de Projeto**: O agente PM coordena e resume todo o processo.

-----

## Opções de Personalização

### Adicionando Novos Agentes

```python
# Em agents.py
new_agent = Agent(
    role="Papel do Seu Agente",
    goal="Objetivo específico do agente",
    backstory="Histórico e experiência do agente",
    llm=llm
)
```

### Criando Novas Tarefas

```python
# Em tasks.py
def create_custom_task(parameters):
    return Task(
        description="Descrição da tarefa com requisitos específicos",
        agent=your_agent,
        expected_output="Formato de saída esperado"
    )
```

### Modificando as Configurações do LLM

```python
# Em llm_config.py - ajuste estes parâmetros:
# - temperature: Controla a aleatoriedade (0.0 - 1.0)
# - max_tokens: Comprimento máximo da resposta
# - model: Modelo NVIDIA a ser usado
```

-----

## Solução de Problemas

### Problemas Comuns

1.  **Problemas com a Chave da API**: Certifique-se de que sua chave de API NVIDIA seja válida e tenha créditos suficientes.
2.  **Erros de Importação de Módulo**: Garanta que todas as dependências estejam instaladas no ambiente correto.
3.  **Limitação de Taxa (Rate Limiting)**: A API NVIDIA pode ter limites de taxa - adicione atrasos se necessário.

### Modo de Depuração

Habilite o registro detalhado definindo `verbose=2` na configuração da equipe:

```python
crew = Crew(
    agents=agents,
    tasks=tasks,
    verbose=2 # Verbose máximo
)
```

-----

## Próximos Passos

1.  **Experimente diferentes tópicos** para ver como os agentes se adaptam.
2.  **Adicione mais agentes especializados** para domínios específicos.
3.  **Implemente ferramentas** para os agentes acessarem APIs ou bancos de dados externos.
4.  **Crie fluxos de trabalho paralelos** para tarefas independentes.
5.  **Adicione recursos de memória e aprendizado** aos agentes.

-----

## Contribuindo

Sinta-se à vontade para estender este projeto por:

  - Adicionar novos tipos de agentes
  - Criar tarefas especializadas
  - Implementar integrações de ferramentas externas
  - Melhorar o tratamento de erros e o registro