#!/bin/bash

# Script de instalação para o Sistema de Análise de Relatórios de Segurança
# Automatiza a configuração do ambiente e instalação das dependências

set -e  # Parar execução se houver erro

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Função para print colorido
print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

print_header() {
    echo -e "${BLUE}$1${NC}"
}

# Header
clear
print_header "🔒 Sistema de Análise Automatizada de Relatórios de Segurança"
print_header "📅 Instalação - $(date '+%Y-%m-%d %H:%M:%S')"
echo ""

# Verificar Python
print_status "Verificando instalação do Python..."
if ! command -v python3 &> /dev/null; then
    print_error "Python 3 não encontrado! Instale Python 3.8+ antes de continuar."
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
print_status "Python detectado: $PYTHON_VERSION"

# Verificar pip
print_status "Verificando pip..."
if ! command -v pip3 &> /dev/null; then
    print_error "pip3 não encontrado! Instale pip3 antes de continuar."
    exit 1
fi

# Criar ambiente virtual (opcional)
read -p "Deseja criar um ambiente virtual? [y/N]: " create_venv
if [[ $create_venv =~ ^[Yy]$ ]]; then
    print_status "Criando ambiente virtual..."
    python3 -m venv venv
    source venv/bin/activate
    print_status "Ambiente virtual ativado."
fi

# Atualizar pip
print_status "Atualizando pip..."
pip3 install --upgrade pip

# Instalar dependências
print_status "Instalando dependências do requirements.txt..."
if [ -f "requirements.txt" ]; then
    pip3 install -r requirements.txt
    print_status "Dependências instaladas com sucesso!"
else
    print_error "Arquivo requirements.txt não encontrado!"
    exit 1
fi

# Criar diretórios necessários
print_status "Criando estrutura de diretórios..."
mkdir -p reports output temp logs

# Configurar arquivo .env
print_status "Configurando arquivo de ambiente..."
if [ ! -f ".env" ]; then
    if [ -f ".env.example" ]; then
        cp .env.example .env
        print_warning "Arquivo .env criado a partir do .env.example"
        print_warning "IMPORTANTE: Edite o arquivo .env com suas configurações!"
    else
        print_error "Arquivo .env.example não encontrado!"
    fi
else
    print_status "Arquivo .env já existe."
fi

# Verificar se Ollama está disponível (para LLM local)
print_status "Verificando disponibilidade do Ollama..."
if command -v ollama &> /dev/null; then
    print_status "Ollama encontrado! Você pode usar modelos locais."
    
    # Verificar se o modelo está disponível
    if ollama list | grep -q "llama"; then
        print_status "Modelo Llama detectado no Ollama."
    else
        print_warning "Nenhum modelo Llama encontrado no Ollama."
        read -p "Deseja baixar o modelo llama3.1? [y/N]: " download_model
        if [[ $download_model =~ ^[Yy]$ ]]; then
            print_status "Baixando modelo llama3.1 (isso pode demorar)..."
            ollama pull llama3.1
        fi
    fi
else
    print_warning "Ollama não encontrado. Configure uma API key do OpenAI no arquivo .env"
fi

# Testar parsers (opcional)
read -p "Deseja executar os testes dos parsers? [y/N]: " run_tests
if [[ $run_tests =~ ^[Yy]$ ]]; then
    print_status "Executando testes dos parsers..."
    python3 test_parsers.py
fi

# Tornar scripts executáveis
print_status "Configurando permissões dos scripts..."
chmod +x security_report_analyzer.py
chmod +x test_parsers.py

# Verificar instalação
print_status "Verificando instalação..."
python3 -c "
try:
    import crewai
    import langchain
    import openai
    print('✅ Todas as dependências principais estão instaladas')
except ImportError as e:
    print(f'❌ Erro na importação: {e}')
    exit(1)
"

# Instruções finais
echo ""
print_header "🎉 Instalação Concluída!"
echo ""
print_status "Próximos passos:"
echo "1. Edite o arquivo .env com suas configurações de API"
echo "2. Coloque seus relatórios de segurança na pasta 'reports/'"
echo "3. Execute: python3 security_report_analyzer.py"
echo ""

print_status "Arquivos de exemplo disponíveis em: examples/"
print_status "- nmap_sample.txt"
print_status "- nessus_sample.xml"  
print_status "- wireshark_sample.log"
echo ""

print_status "Para testar o sistema:"
echo "python3 security_report_analyzer.py"
echo ""

if [[ $create_venv =~ ^[Yy]$ ]]; then
    print_warning "Lembre-se de ativar o ambiente virtual:"
    print_warning "source venv/bin/activate"
fi

print_header "📚 Documentação completa disponível no README.md"
echo ""
