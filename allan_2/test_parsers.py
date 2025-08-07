#!/usr/bin/env python3
"""
Script de teste para validar os parsers de relatórios de segurança
"""

import os
import json
import sys
from pathlib import Path

# Adicionar o diretório atual ao path para importar os módulos
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from report_parsers import ReportParserFactory

def test_parsers():
    """Testa todos os parsers com os arquivos de exemplo"""
    
    examples_dir = Path("examples")
    test_files = [
        ("nmap_sample.txt", "Nmap"),
        ("nessus_sample.xml", "Nessus"),
        ("wireshark_sample.log", "Wireshark")
    ]
    
    print("🧪 Testando Parsers de Relatórios de Segurança")
    print("=" * 50)
    
    for filename, tool_name in test_files:
        file_path = examples_dir / filename
        
        if not file_path.exists():
            print(f"❌ Arquivo não encontrado: {file_path}")
            continue
        
        print(f"\n📄 Testando {tool_name}: {filename}")
        print("-" * 30)
        
        try:
            # Parse do arquivo
            vulnerabilities = ReportParserFactory.parse_report(str(file_path))
            
            if not vulnerabilities:
                print(f"⚠️  Nenhuma vulnerabilidade encontrada em {filename}")
                continue
            
            print(f"✅ {len(vulnerabilities)} vulnerabilidades encontradas")
            
            # Mostrar estatísticas
            tipos = {}
            severidades = {}
            
            for vuln in vulnerabilities:
                # Contar tipos
                tipo = vuln.get('tipo_preliminar', 'Desconhecido')
                tipos[tipo] = tipos.get(tipo, 0) + 1
                
                # Contar severidades
                sev = vuln.get('severidade', 'Não definido')
                severidades[sev] = severidades.get(sev, 0) + 1
            
            print(f"📊 Distribuição por tipo:")
            for tipo, count in tipos.items():
                print(f"   • {tipo}: {count}")
            
            print(f"📊 Distribuição por severidade:")
            for sev, count in severidades.items():
                print(f"   • {sev}: {count}")
            
            # Mostrar algumas vulnerabilidades como exemplo
            print(f"\n🔍 Primeiras 3 vulnerabilidades:")
            for i, vuln in enumerate(vulnerabilities[:3]):
                print(f"   {i+1}. [{vuln['id']}] {vuln['titulo']}")
                print(f"      Tipo: {vuln['tipo_preliminar']} | Severidade: {vuln.get('severidade', 'N/A')}")
                if vuln.get('ip_origem'):
                    print(f"      IP: {vuln['ip_origem']}")
                if vuln.get('porta'):
                    print(f"      Porta: {vuln['porta']}")
                print()
            
            # Salvar resultado em JSON para inspeção
            output_file = f"test_output_{tool_name.lower()}.json"
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(vulnerabilities, f, indent=2, ensure_ascii=False)
            
            print(f"💾 Resultado salvo em: {output_file}")
            
        except Exception as e:
            print(f"❌ Erro ao processar {filename}: {str(e)}")
            import traceback
            traceback.print_exc()

def test_vulnerability_classification():
    """Testa a classificação automática de vulnerabilidades"""
    
    print("\n🎯 Testando Classificação de Vulnerabilidades")
    print("=" * 50)
    
    from report_parsers import BaseParser
    
    parser = BaseParser()
    
    test_cases = [
        ("SQL injection vulnerability in login form", "Web"),
        ("SSH service running on non-standard port", "Rede"),
        ("Windows kernel privilege escalation", "Infraestrutura"),
        ("Cross-site scripting in user input", "Web"),
        ("Open FTP service allows anonymous access", "Rede"),
        ("Missing security patches on Linux server", "Infraestrutura"),
        ("Apache server information disclosure", "Web"),
        ("SNMP community string misconfiguration", "Rede"),
        ("Weak file permissions on system files", "Infraestrutura")
    ]
    
    for description, expected_type in test_cases:
        classified_type = parser.classify_vulnerability_type(description)
        status = "✅" if classified_type == expected_type else "❌"
        print(f"{status} '{description[:50]}...'")
        print(f"    Esperado: {expected_type} | Obtido: {classified_type}")
        print()

def main():
    """Função principal"""
    
    print("🚀 Iniciando Testes do Sistema de Análise de Segurança")
    print("🗓️  Data:", "07 de Agosto de 2025")
    print()
    
    # Verificar se os arquivos de exemplo existem
    examples_dir = Path("examples")
    if not examples_dir.exists():
        print("❌ Diretório 'examples' não encontrado!")
        print("Execute o script a partir da raiz do projeto.")
        return
    
    # Testar parsers
    test_parsers()
    
    # Testar classificação
    test_vulnerability_classification()
    
    print("\n🎉 Testes concluídos!")
    print("📁 Verifique os arquivos 'test_output_*.json' para detalhes completos.")

if __name__ == "__main__":
    main()
