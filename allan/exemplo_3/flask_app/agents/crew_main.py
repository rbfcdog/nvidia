from crewai import Crew, Process
from agent import *
from tasks import *
import os
import time

def create_optimized_security_crew():
    """
    Create optimized crew for fast security analysis
    """
    
    # Ensure output directories exist
    os.makedirs("outputs", exist_ok=True)
    os.makedirs("outputs/report_sections", exist_ok=True)
    os.makedirs("input", exist_ok=True)
    
    # Optimized crew with minimal overhead
    crew = Crew(
        agents=[analizador_agent, especialista_rede, especialista_web, especialista_infra, redator_executivo],
        tasks=[task_estruturar_relatorio, task_rede, task_web, task_infra, task_relatorio_final],
        process=Process.sequential,  # Sequential é mais previsível que hierarchical
        verbose=False,  # Reduzir logs para acelerar
        memory=False,  # Desabilitar memória para reduzir overhead
        max_execution_time=900  # 15 minutos máximo total
    )
    
    return crew

def run_optimized_analysis(raw_report_path=None):
    """
    Run optimized security analysis with timing
    """
    print("🚀 Starting Optimized Security Analysis")
    print("=" * 50)
    
    # Check input file
    if raw_report_path is None:
        raw_report_path = "input/recon_raw_output.txt"
    
    if not os.path.exists(raw_report_path):
        print(f"❌ Input file not found: {raw_report_path}")
        return None
    
    start_time = time.time()
    
    try:
        # Create and execute optimized crew
        crew = create_optimized_security_crew()
        
        print("⚡ Executing analysis pipeline...")
        result = crew.kickoff()
        
        execution_time = time.time() - start_time
        
        print(f"\n✅ Analysis completed in {execution_time:.1f} seconds")
        print("\n📄 Generated files:")
        print("  • outputs/structured_analysis.json")
        print("  • outputs/report_sections/network_findings.md")
        print("  • outputs/report_sections/web_findings.md") 
        print("  • outputs/report_sections/infra_findings.md")
        print("  • outputs/pentest_report.md")
        
        return result
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return None

def create_sample_input():
    """Create optimized sample input"""
    sample_content = """Nmap scan report for 192.168.1.100
22/tcp   open  ssh        OpenSSH 7.2p2 Ubuntu
80/tcp   open  http       Apache httpd 2.4.18
443/tcp  open  ssl/http   Apache httpd 2.4.18
21/tcp   open  ftp        vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed
3306/tcp open  mysql      MySQL 5.7.31
445/tcp  open  netbios-ssn Samba smbd 4.3.11
"""
    
    os.makedirs("input", exist_ok=True)
    with open("input/recon_raw_output.txt", "w") as f:
        f.write(sample_content)
    
    print("📝 Sample input created: input/recon_raw_output.txt")

if __name__ == "__main__":
    print("🔒 Optimized Security Analysis Tool")
    print("=" * 35)
    
    choice = input("1. Run with existing input\n2. Create sample and run\n3. Custom input path\nChoice (1-3): ")
    
    if choice == "1":
        run_optimized_analysis()
    elif choice == "2":
        create_sample_input()
        run_optimized_analysis()
    elif choice == "3":
        path = input("Input file path: ").strip()
        if path:
            run_optimized_analysis(path)
    else:
        print("Invalid choice!")