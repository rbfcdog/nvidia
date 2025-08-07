# Análise de Vulnerabilidades Web  

Abaixo está a análise detalhada das vulnerabilidades web identificadas no `structured_analysis.json`, com classificação OWASP Top 10, cenários de exploração, impactos técnicos e soluções práticas imediatas.  

---

## **Vulnerabilidade 2: Web Server Exposing Server Version in HTTP Headers**  
**Porta:** 80  
**Serviço:** HTTP (Apache 2.4.41)  

### **1. Classificação OWASP Top 10**  
**A05:2021 - Security Misconfiguration**  
Justificativa: Exposição de detalhes do servidor (ex: versão do Apache) via cabeçalhos HTTP facilita a identificação de vulnerabilidades específicas pelo atacante.  

### **2. Scenario de Exploração**  
Atacantes extraem a versão do servidor (`Server: Apache/2.4.41`) através de uma requisição HTTP simples (ex: usando `curl` ou ferramentas como Burp Suite). Com essa informação, buscam exploits conhecidos para a versão exata do Apache ou do sistema operacional (Ubuntu), como falhas de segurança não corrigidas.  

### **3. Impacto Técnico Direto**  
- **Facilitação de ataques direcionados**: O atacante pode explorar vulnerabilidades específicas da versão do Apache (ex: CVE-2021-44228 para versões desatualizadas).  
- **Reconhecimento de sistema**: Permite mapear o ambiente para ataques posteriores (ex: path traversal, RCE).  
- **Aumento da superfície de ataque**: Informações desnecessárias expostas ajudam no planejamento de exploits.  

### **4. Correção Prática**  

#### **Código Seguro (Configuração Apache)**  
Edite o arquivo de configuração do Apache (`/etc/apache2/apache2.conf` ou `/etc/httpd/conf/httpd.conf`) e adicione as seguintes diretivas para ocultar informações sensíveis:  

```apache
# Ocultar versão do servidor e sistema operacional  
ServerTokens Prod  
ServerSignature Off  

# Reiniciar serviço Apache  
sudo systemctl restart apache2  
```  

#### **Headers de Segurança Adicionais**  
Adicione headers HTTP para proteção contra outros vetores OWASP:  

```apache
# Adicionar no final do arquivo de configuração  
<IfModule mod_headers.c>  
    # Proteção contra MIME Sniffing  
    Header always set X-Content-Type-Options "nosniff"  

    # Proteção contra Clickjacking  
    Header always set X-Frame-Options "DENY"  

    # Proteção contra XSS  
    Header always set Content-Security-Policy "default-src 'self'; script-src 'self' 'unsafe-inline'"  

    # Proteção contra cache de conteúdo sensível  
    Header always set Cache-Control "no-store, no-cache, must-revalidate"  
</IfModule>  
```  

#### **Validação Pós-Correção**  
Use `curl` para verificar se o header `Server` não revela detalhes:  

```bash  
curl -I http://localhost  
# Saída esperada:  
# Server: Apache  
# (sem versão ou sistema operacional)  
```  

---

## **Resumo**  
| ID | Vulnerabilidade                          | OWASP Top 10       | Mitigação Chave                          |  
|----|------------------------------------------|-------------------|------------------------------------------|  
| 2  | Exposição de versão do servidor HTTP     | A05:2021          | Ocultar headers via configuração Apache |  

**Nota:** Após aplicar as correções, execute um novo scan (ex: com `nmap --script http-headers`) para validação.  

---  

**Observação:** Nenhum outro finding do `structured_analysis.json` foi classificado como `type="web"`. A análise foi focada exclusivamente na vulnerabilidade web identificada.