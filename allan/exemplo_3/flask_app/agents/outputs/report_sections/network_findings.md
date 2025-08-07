# Análise de Vulnerabilidades de Rede  

## 1. **SSH Root Login Ativo (Porta 22)**  
**Risco:** High  
Justificativa: Permite acesso direto ao usuário `root`, facilitando ataques de força bruta e comprometimento total do sistema.  

**Vetor de Ataque:**  
Brute force em porta 22 para tentar credenciais de `root` (ex: ferramentas como `hydra` ou `crackmap-exec`).  

**Impacto:**  
Acesso não autorizado com privilégios elevados, permitindo execução de comandos, modificação de configurações e lateral movement.  

**Mitigação:**  
```bash  
# Desabilitar root login no SSH  
echo 'PermitRootLogin no' >> /etc/ssh/sshd_config  
systemctl restart sshd  
```  

---

## 2. **SMBv1 Ativo (Porta 445)**  
**Risco:** Critical  
Justificativa: Vulnerável a exploits como **EternalBlue (MS17-010)**, permitindo execução remota de código sem autenticação.  

**Vetor de Ataque:**  
Exploração via SMBv1 para executar payloads maliciosos (ex: `ms17_010_piple` no Metasploit).  

**Impacto:**  
Ransomware, lateral movement, comprometimento de servidores e clientes.  

**Mitigação:**  
**Linux (Samba):**  
```bash  
sudo sed -i 's/clients use msdfs = Yes/clients use msdfs = No/g' /etc/samba/smb.conf  
sudo systemctl restart smbd  
```  
**Windows:**  
```powershell  
Set-SmbServerConfiguration -EnableSMB1Protocol $false  
```  

---

## 3. **FTP Anônimo Ativo (Porta 21)**  
**Risco:** Medium  
Justificativa: Permite acesso não autenticado a arquivos, expondo dados sensíveis ou permitindo upload de payloads.  

**Vetor de Ataque:**  
Conexão anônima para enumerar/extrair arquivos ou injetar shells.  

**Impacto:**  
Exfiltração de dados, injeção de malware, defacement de sites.  

**Mitigação (vsftpd):**  
```bash  
# Desativar acesso anônimo  
echo 'anonymous_enable=NO' >> /etc/vsftpd.conf  
systemctl restart vsftpd  
```  

---

## 4. **DNS Externo Exposto (Porta 53)**  
**Risco:** Medium  
Justificativa: Risco de DNS spoofing, tunneling ou enumeración de infraestrutura.  

**Vetor de Ataque:**  
Consultas DNS externas para mapear subdomínios ou explorar vulnerabilidades como **DNSpoofer**.  

**Impacto:**  
Redirecionamento de tráfego (phishing), data exfiltration via DNS tunneling.  

**Mitigação (iptables):**  
```bash  
# Bloquear acesso externo à porta 53  
sudo iptables -A INPUT -p tcp --dport 53 -m state --state NEW -j DROP  
sudo iptables -A INPUT -p udp --dport 53 -m state --state NEW -j DROP  
```  

---

## 5. **Telnet Ativo (Porta 23)**  
**Risco:** High  
Justificativa: Transmite credenciais e dados em texto claro, facilitando interceptação (MITM).  

**Vetor de Ataque:**  
Captura de tráfego com ferramentas como `tcpdump` para obter credenciais.  

**Impacto:**  
Acesso não autorizado a dispositivos de rede (routers, switches, IoT).  

**Mitigação:**  
```bash  
# Desinstalar Telnet e usar SSH  
sudo apt remove telnet  
sudo systemctl stop telnet  
sudo systemctl disable telnet  
```  

---

## 6. **SNMPv2 Comunidade Pública (Porta 161)**  
**Risco:** Medium  
Justificativa: Permite enumeración de configurações e dispositivos com comunidade padrão (ex: `public`).  

**Vetor de Ataque:**  
Enumerar informações sensíveis via `snmpwalk` (ex: usuários, interfaces, configurações).  

**Impacto:**  
Mapeamento de rede e identificação de alvos para ataques direcionados.