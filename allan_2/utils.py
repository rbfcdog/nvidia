#!/usr/bin/env python3
"""
Utilitários para o sistema de análise de relatórios de segurança
"""

import os
import json
import shutil
import argparse
from datetime import datetime
from pathlib import Path
from typing import Dict, List

def clean_output_files():
    """Remove todos os arquivos de saída gerados"""
    output_files = [
        "vulnerabilities.json",
        "network_analysis.md",
        "web_analysis.md", 
        "infra_analysis.md",
        "relatorio_final_seguranca.md",
        "test_output_nmap.json",
        "test_output_nessus.json",
        "test_output_wireshark.json"
    ]
    
    removed_count = 0
    for file in output_files:
        if os.path.exists(file):
            os.remove(file)
            print(f"🗑️  Removido: {file}")
            removed_count += 1
    
    # Limpar diretório output se existir
    output_dir = Path("output")
    if output_dir.exists():
        for file in output_dir.glob("*"):
            if file.is_file():
                file.unlink()
                print(f"🗑️  Removido: {file}")
                removed_count += 1
    
    print(f"✅ {removed_count} arquivos removidos")

def clean_temp_files():
    """Remove arquivos temporários"""
    temp_dirs = ["temp", "logs", "__pycache__"]
    removed_count = 0
    
    for temp_dir in temp_dirs:
        if os.path.exists(temp_dir):
            if temp_dir == "__pycache__":
                shutil.rmtree(temp_dir)
                print(f"🗑️  Removido diretório: {temp_dir}")
                removed_count += 1
            else:
                # Limpar conteúdo mas manter diretório
                for file in Path(temp_dir).glob("*"):
                    if file.is_file():
                        file.unlink()
                        removed_count += 1
    
    print(f"✅ {removed_count} arquivos temporários removidos")

def generate_sample_report():
    """Gera um relatório de amostra para teste"""
    sample_vulnerabilities = [
        {
            "id": "SAMPLE-001",
            "titulo": "Porta SSH aberta com configuração insegura",
            "descricao": "O serviço SSH está executando na porta padrão 22 com configurações que podem permitir ataques de força bruta.",
            "tipo_preliminar": "Rede",
            "dados_brutos": "22/tcp open ssh OpenSSH 7.4",
            "ip_origem": "192.168.1.100",
            "porta": "22",
            "protocolo": "tcp",
            "severidade": "Médio"
        },
        {
            "id": "SAMPLE-002", 
            "titulo": "Servidor web expondo informações de versão",
            "descricao": "O servidor Apache está retornando informações detalhadas sobre sua versão, facilitando ataques direcionados.",
            "tipo_preliminar": "Web",
            "dados_brutos": "80/tcp open http Apache httpd 2.4.6",
            "ip_origem": "192.168.1.100",
            "porta": "80", 
            "protocolo": "tcp",
            "severidade": "Baixo"
        },
        {
            "id": "SAMPLE-003",
            "titulo": "Banco MySQL acessível externamente",
            "descricao": "O serviço MySQL está executando na porta 3306 e pode estar acessível da internet, representando um risco crítico de segurança.",
            "tipo_preliminar": "Infraestrutura",
            "dados_brutos": "3306/tcp open mysql MySQL 5.7.26",
            "ip_origem": "192.168.1.100",
            "porta": "3306",
            "protocolo": "tcp", 
            "severidade": "Alto"
        }
    ]
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"sample_report_{timestamp}.txt"
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("# Relatório de Segurança de Amostra\n")
        f.write(f"# Gerado em: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        for vuln in sample_vulnerabilities:
            f.write(f"Vulnerability: {vuln['titulo']}\n")
            f.write(f"Type: {vuln['tipo_preliminar']}\n")
            f.write(f"Severity: {vuln['severidade']}\n")
            f.write(f"Host: {vuln['ip_origem']}:{vuln['porta']}\n")
            f.write(f"Description: {vuln['descricao']}\n")
            f.write(f"Raw Data: {vuln['dados_brutos']}\n")
            f.write("\n" + "="*50 + "\n\n")
    
    print(f"✅ Relatório de amostra gerado: {filename}")
    return filename

def validate_environment():
    """Valida se o ambiente está configurado corretamente"""
    print("🔍 Validando ambiente...")
    
    issues = []
    
    # Verificar arquivos essenciais
    required_files = [
        "security_report_analyzer.py",
        "config.py", 
        "report_parsers.py",
        "requirements.txt"
    ]
    
    for file in required_files:
        if not os.path.exists(file):
            issues.append(f"Arquivo ausente: {file}")
    
    # Verificar diretórios
    required_dirs = ["examples", "reports", "output", "temp", "logs"]
    for directory in required_dirs:
        if not os.path.exists(directory):
            try:
                os.makedirs(directory)
                print(f"📁 Criado diretório: {directory}")
            except Exception as e:
                issues.append(f"Erro ao criar diretório {directory}: {e}")
    
    # Verificar dependências Python
    try:
        import crewai
        print("✅ CrewAI importado com sucesso")
    except ImportError:
        issues.append("CrewAI não instalado - execute: pip install crewai")
    
    try:
        import langchain
        print("✅ LangChain importado com sucesso")
    except ImportError:
        issues.append("LangChain não instalado - execute: pip install langchain")
    
    # Verificar arquivo .env
    if not os.path.exists(".env"):
        if os.path.exists(".env.example"):
            shutil.copy(".env.example", ".env")
            print("📝 Arquivo .env criado a partir do .env.example")
            issues.append("Configure o arquivo .env com suas credenciais")
        else:
            issues.append("Arquivo .env não encontrado")
    
    # Relatório final
    if issues:
        print("\n❌ Problemas encontrados:")
        for issue in issues:
            print(f"   • {issue}")
        return False
    else:
        print("\n✅ Ambiente validado com sucesso!")
        return True

def show_statistics():
    """Mostra estatísticas dos arquivos no projeto"""
    print("📊 Estatísticas do Projeto")
    print("=" * 30)
    
    # Contar arquivos por tipo
    file_types = {
        ".py": 0,
        ".md": 0, 
        ".txt": 0,
        ".xml": 0,
        ".json": 0,
        ".log": 0,
        ".sh": 0,
        "outros": 0
    }
    
    total_files = 0
    total_size = 0
    
    for root, dirs, files in os.walk("."):
        # Ignorar diretórios específicos
        if any(ignore in root for ignore in [".git", "__pycache__", "venv", ".env"]):
            continue
            
        for file in files:
            file_path = os.path.join(root, file)
            total_files += 1
            
            try:
                size = os.path.getsize(file_path)
                total_size += size
            except:
                continue
            
            # Classificar por extensão
            ext = os.path.splitext(file)[1].lower()
            if ext in file_types:
                file_types[ext] += 1
            else:
                file_types["outros"] += 1
    
    print(f"Total de arquivos: {total_files}")
    print(f"Tamanho total: {total_size / 1024:.1f} KB")
    print("\nDistribuição por tipo:")
    
    for ext, count in file_types.items():
        if count > 0:
            print(f"  {ext}: {count} arquivos")
    
    # Verificar exemplos
    examples_dir = Path("examples")
    if examples_dir.exists():
        example_files = list(examples_dir.glob("*"))
        print(f"\nArquivos de exemplo: {len(example_files)}")
        for file in example_files:
            size_kb = file.stat().st_size / 1024
            print(f"  • {file.name}: {size_kb:.1f} KB")

def main():
    """Função principal com CLI"""
    parser = argparse.ArgumentParser(
        description="Utilitários para o Sistema de Análise de Relatórios de Segurança"
    )
    
    parser.add_argument(
        "action",
        choices=["clean", "clean-temp", "sample", "validate", "stats"],
        help="Ação a ser executada"
    )
    
    args = parser.parse_args()
    
    print("🛠️  Utilitários do Sistema de Análise de Segurança")
    print("=" * 50)
    
    if args.action == "clean":
        print("🧹 Limpando arquivos de saída...")
        clean_output_files()
        
    elif args.action == "clean-temp":
        print("🧹 Limpando arquivos temporários...")
        clean_temp_files()
        
    elif args.action == "sample":
        print("📝 Gerando relatório de amostra...")
        filename = generate_sample_report()
        print(f"Use este arquivo para testar: python3 security_report_analyzer.py")
        
    elif args.action == "validate":
        print("🔍 Validando ambiente...")
        if validate_environment():
            print("Ambiente pronto para uso!")
        else:
            print("Corrija os problemas antes de prosseguir.")
            
    elif args.action == "stats":
        show_statistics()

if __name__ == "__main__":
    main()
