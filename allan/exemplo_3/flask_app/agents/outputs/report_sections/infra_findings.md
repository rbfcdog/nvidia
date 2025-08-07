</think>

# Relatório de Vulnerabilidades Web  

## 1. **SQL Injection (SQLi)**  
**Classificação OWASP:** A03:2021 - Injection  
**Scenario de Exploração:**  
Um formulário de login utiliza entrada do usuário diretamente em uma consulta SQL sem sanitização:  
```php
// Código vulnerável
$query = "SELECT * FROM users WHERE username = '$username' AND password = '$password'";
```
Um atacante insere `' OR '1'='1` como senha, logando como qualquer usuário.  

**Impacto Técnico:**  
- Exposição de dados sensíveis (ex: senhas, informações financeiras).  
- Manipulação de dados (alteração de saldos, exclusão de registros).  
- Bypass de autenticação.  

**Correção Prática:**  
- **Código Seguro (Python com psycopg2):**  
  ```python
  cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
  ```
- **Validação de Entrada:**  
  ```python
  import re
  if not re.match("^[a-zA-Z0-9_]{3,20}$", username):
      raise ValueError("Username inválido")
  ```
- **Web Application Firewall (WAF):**  
  Configure regras para bloquear padrões de SQLi (ex: `UNION`, `DROP`).  

---

## 2. **Cross-Site Scripting (XSS)**  
**Classificação OWASP:** A03:2021 - Injection  
**Scenario de Exploração:**  
Um campo de comentários reflete entrada do usuário sem sanitização:  
```html
<!-- Código vulnerável -->
<div>Comentário: <?php echo $_GET['comment']; ?></div>
```
Atacante insere `<script>alert('XSS')</script>`, executando código no contexto do usuário.  

**Impacto Técnico:**  
- Roubo de cookies/sessões (session hijacking).  
- Redirecionamento para sites maliciosos.  
- Defacement de páginas.  

**Correção Prática:**  
- **Sanitização de Saída (JavaScript):**  
  ```javascript
  // Usando DOMPurify
  document.getElementById('comment').innerHTML = DOMPurify.sanitize(userInput);
  ```
- **Content Security Policy (CSP):**  
  ```http
  Content-Security-Policy: script-src 'self'; object-src 'none'
  ```
- **Codificação de Saída (PHP):**  
  ```php
  echo htmlspecialchars($_GET['comment'], ENT_QUOTES, 'UTF-8');
  ```

---

## 3. **Cross-Site Request Forgery (CSRF)**  
**Classificação OWASP:** A08:2021 - Software and Data Integrity Failures  
**Scenario de Exploração:**  
Um formulário de alteração de email não utiliza token CSRF:  
```html
<form action="/change_email" method="POST">
  <input type="email" name="new_email">
  <input type="submit" value="Enviar">
</form>
```
Atacante engana a vítima em submeter o formulário via `<img src="https://vulnerable.com/change_email?new_email=attacker@example.com">`.  

**Impacto Técnico:**  
- Alteração não autorizada de dados (ex: email, senha).  
- Transferência de fundos em sistemas bancários.  

**Correção Prática:**  
- **Token CSRF no Backend (Node.js):**  
  ```javascript
  // Express.js
  const csrf = require('csurf');
  const csrfProtection = csrf({ cookie: true });
  app.post('/change_email', csrfProtection, (req, res) => {
    // Processar alteração
  });
  ```
- **Cookies com SameSite:**  
  ```http
  Set-Cookie: session=abc123; SameSite=Strict; HttpOnly; Secure
  ```

---

## 4. **Security Misconfiguration (Debug Mode Ativo)**  
**Classificação OWASP:** A05:2021 - Security Misconfiguration  
**Scenario de Exploração:**  
Modo debug ativado em produção exibe traces de erro com informações sensíveis:  
```python
# Flask configuração perigosa
app.config['DEBUG'] = True
```
Atacante aciona uma exceção (ex: acesso a rota inexistente) e obtém caminhos do sistema, versões de bibliotecas.  

**Impacto Técnico:**  
- Facilita ataques de exploit (ex: RCE em bibliotecas desatualizadas).  
- Enumeração de estrutura do servidor.  

**Correção Prática:**  
- **Desativar Debug em Produção (Flask):**  
  ```python
  app.config['DEBUG'] = False
  ```
- **Configuração de Servidor (N