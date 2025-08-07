# 🚀 Guia de Início Rápido

Este guia vai te ajudar a configurar e executar o sistema em poucos minutos.

## ⚡ Instalação Automática

```bash
# Executar script de instalação
./install.sh
```

O script irá:
- ✅ Verificar dependências
- ✅ Instalar pacotes Python
- ✅ Criar estrutura de diretórios
- ✅ Configurar arquivo .env
- ✅ Testar instalação

## 🔧 Configuração Manual Rápida

Se preferir configurar manualmente:

### 1. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 2. Configurar Ambiente
```bash
cp .env.example .env
# Edite .env com suas configurações
```

### 3. Testar Parsers
```bash
python3 test_parsers.py
```

## 🎯 Execução Rápida

### Usando Arquivos de Exemplo
```bash
# Testar com exemplo do Nmap
python3 security_report_analyzer.py
# Quando solicitado, digite: examples/nmap_sample.txt

# Testar com exemplo do Nessus  
python3 security_report_analyzer.py
# Quando solicitado, digite: examples/nessus_sample.xml

# Testar com exemplo do Wireshark
python3 security_report_analyzer.py  
# Quando solicitado, digite: examples/wireshark_sample.log
```

### Usando Seus Próprios Relatórios
```bash
# 1. Coloque seu relatório na pasta reports/
cp seu_relatorio.txt reports/

# 2. Execute o analisador
python3 security_report_analyzer.py
# Quando solicitado, digite: reports/seu_relatorio.txt
```

## 📋 Checklist de Configuração

- [ ] Python 3.8+ instalado
- [ ] Dependências instaladas (`pip install -r requirements.txt`)
- [ ] Arquivo `.env` configurado com API key
- [ ] LLM configurada (OpenAI API ou Ollama local)
- [ ] Diretórios criados (reports/, output/, temp/, logs/)
- [ ] Testes executados com sucesso

## 🔑 Configuração de LLM

### Opção 1: OpenAI API
```env
OPENAI_API_KEY=sk-your-key-here
OPENAI_MODEL_NAME=gpt-4
```

### Opção 2: Ollama Local
```bash
# Instalar Ollama
curl -fsSL https://ollama.ai/install.sh | sh

# Baixar modelo
ollama pull llama3.1

# Configurar .env
OPENAI_API_BASE=http://localhost:11434/v1
OPENAI_MODEL_NAME=llama3.1
```

## 🛠️ Utilitários Disponíveis

```bash
# Limpar arquivos gerados
python3 utils.py clean

# Gerar relatório de exemplo
python3 utils.py sample

# Validar configuração
python3 utils.py validate

# Ver estatísticas do projeto
python3 utils.py stats
```

## 📊 Saída Esperada

Após executar, você terá:

1. **`vulnerabilities.json`** - Dados estruturados
2. **`network_analysis.md`** - Análise de rede
3. **`web_analysis.md`** - Análise web
4. **`infra_analysis.md`** - Análise infraestrutura  
5. **`relatorio_final_seguranca.md`** - Relatório final consolidado

## ⚠️ Solução de Problemas

### Erro: "ModuleNotFoundError: No module named 'crewai'"
```bash
pip install crewai crewai-tools
```

### Erro: "OpenAI API key not configured"
- Edite o arquivo `.env` e adicione sua API key
- Ou configure Ollama para uso local

### Erro: "File not found"
- Verifique se o caminho do arquivo está correto
- Use caminhos absolutos se necessário

### LLM muito lenta
- Configure um modelo menor no `.env`
- Aumente o timeout em `ANALYSIS_TIMEOUT`

## 📞 Suporte

- 📖 Documentação completa: `README.md`
- 🧪 Testes: `python3 test_parsers.py`
- 🛠️ Utilitários: `python3 utils.py --help`

---

**🎉 Pronto! Seu sistema está configurado e rodando!**
