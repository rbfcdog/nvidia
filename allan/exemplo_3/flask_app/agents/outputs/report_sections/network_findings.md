# Análise de Vulnerabilidades de Rede  

Abaixo está a análise detalhada das vulnerabilidades de rede identificadas no `structured_analysis.json`, com riscos, vetores de ataque, impactos e soluções técnicas imediatas.  

---

## **Vulnerabilidade 1: SSH Service Running with Default Configuration**  
**Porta:** 22  
**Serviço:** SSH (OpenSSH 8.2p1)  

### **1. Risco: Medium**  
Justificativa: Configurações padrão do SSH podem incluir permissão de login root, uso de criptografia fraca ou ausência de autenticação multifator (MFA). Isso facilita ataques de força bruta ou exploração de falhas de configuração.  

### **2. Vetor de Ataque**  
Atacantes podem explorar a porta 22 via força bruta (ex: tentativas de adivinhar credenciais) ou exploração de falhas no OpenSSH 8.2p1 (se não atualizado).  

### **3. Impacto**  
- Acesso não autorizado ao sistema.  
- Execução remota de comandos ou shell.  
- Movimento lateral na rede interna.  

### **4. Mitigação**  
Edite o arquivo de configuração do SSH (`/etc/ssh/sshd_config`) e aplique as seguintes alterações:  

```bash
# Desabilitar login root  
echo 'PermitRootLogin no' >> /etc/ssh/sshd_config  

# Limitar usuários autorizados (ex: usuário "admin")  
echo 'AllowUsers admin' >> /etc/ssh/sshd_config  

# Usar criptografia forte  
echo 'KexAlgorithms curve25519-sha256,ecdh-sha2-nistp256' >> /etc/ssh/sshd_config  
echo 'Ciphers chacha20-poly1305@openssh.com,aes256-gcm@openssh.com' >> /etc/ssh/sshd_config  
echo 'MACs hmac-sha2-512-etm@openssh.com,hmac-sha2-256-etm@openssh.com' >> /etc/ssh/sshd_config  

# Reiniciar serviço SSH  
systemctl restart sshd  
```  

---

## **Vulnerabilidade 3: SMB Service Vulnerable to EternalBlue (MS17-010)**  
**Porta:** 445  
**Serviço:** SMB (Samba 4.11.13)  

### **1. Risco: Critical**  
Justificativa: SMBv1 é conhecido por vulnerabilidades críticas (ex: EternalBlue), permitindo execução remota de código sem autenticação.  

### **2. Vetor de Ataque**  
Atacantes exploram a vulnerabilidade SMBv1 (MS17-010) para executar código arbitrário no servidor, muitas vezes sem necessidade de credenciais.  

### **3. Impacto**  
- Ransomware ou malware implantado.  
- Acesso total ao sistema.  
- Comprometimento da rede interna.  

### **4. Mitigação**  
Desative SMBv1 e atualize o Samba para uma versão corrigida:  

```bash
# Editar smb.conf  
sudo nano /etc/samba/smb.conf  

# Adicionar no final do arquivo:  
[global]  
   min protocol = SMB2  
   max protocol = SMB3  

# Reiniciar Samba  
sudo systemctl restart smbd  

# Verificar versão atualizada (deve ser >= 4.11.14 ou 4.12.x)  
smbd -V  
```  

---

## **Vulnerabilidade 6: FTP Service Allowing Anonymous Login**  
**Porta:** 21  
**Serviço:** FTP (vsftpd 3.0.3)  

### **1. Risco: High**  
Justificativa: Login anônimo permite acesso não autorizado a arquivos, facilitando upload de malware ou vazamento de dados.  

### **2. Vetor de Ataque**  
Atacantes conectam-se ao FTP com `anonymous` como usuário e qualquer senha, explorando permissões indevidas.  

### **3. Impacto**  
- Modificação ou exclusão de arquivos críticos.  
- Uso do servidor como pivot para ataques internos.  
- Vazamento de dados sensíveis.  

### **4. Mitigação**  
Desative o login anônimo no `vsftpd.conf`:  

```bash
# Editar configuração do vsftpd  
sudo nano /etc/vsftpd.conf  

# Alterar ou adicionar:  
anonymous_enable=NO  
local_enable=YES  
write_enable=YES  

# Reiniciar serviço FTP  
sudo systemctl restart vsftpd  
```  

---  

## **Resumo**  
| ID | Vulnerabilidade                  | Risco   | Mitigação Chave                          |  
|----|-----------------------------------|---------|------------------------------------------|  
| 1  | SSH Default Config                | Medium  | Desativar root login e usar criptografia |  
| 3  | SMB EternalBlue (MS17-010)        | Critical | Desativar SMBv1 e atualizar Samba       |  
| 6  | FTP Anonymous Login               | High    | Desativar `anonymous_enable`            |  

**Nota:** Após aplicar as correções, execute um novo scan para validação.