executor_agent = Agent(
    role="Advanced Offensive Security Technician",
    goal="Execute network and service scans to collect raw data",
    backstory=(
        "You are a cybersecurity professional focused on reconnaissance. "
        "You use command-line tools like Nmap to map attack surfaces, "
        "identifying open ports, services, versions, and configurations. "
        "You follow instructions precisely."
    ),
    tools=[],
    llm=llm,
    verbose=True,
    allow_delegation=False
)

task_recon = Task(
    description=f"""
    Check if 'pentest_report.md' exists in outputs/. If it does, analyze it and determine what deeper scans or specific service tests should be run next.
    Otherwise, perform a comprehensive Nmap scan on the target: '{TARGET}'.
    Use command: nmap -sV -sC -p- {TARGET}
    Save the full output to 'outputs/recon_raw_output.txt'.
    Do not summarize — provide raw scan data.
    """,
    expected_output="A file named 'recon_raw_output.txt' containing the complete Nmap output.",
    agent=executor_agent,
    output_file="outputs/recon_raw_output.txt"
)

analyst_agent = Agent(
    role="Threat Intelligence Analyst",
    goal="Interpret raw scan data and structure it into JSON",
    backstory=(
        "You are a meticulous analyst who turns chaotic logs into actionable intelligence. "
        "You identify relevant data: ports, services, versions, web tech — filtering out noise."
    ),
    llm=llm,
    verbose=True,
    allow_delegation=False
)

task_analyze = Task(
    description="""
    Analyze the file 'outputs/recon_raw_output.txt'. Extract:
    - All open ports
    - Service names and versions
    - Host status (up/down)
    - Detected scripts (e.g., http-title, ssl-cert)
    - Web technologies (if any)
    Structure this into a clean JSON format.
    Do not include explanations — just data.
    """,
    expected_output="A JSON file 'outputs/structured_analysis.json' with structured scan results.",
    agent=analyst_agent,
    output_file="outputs/structured_analysis.json"
)

network_specialist = Agent(
    role="Senior Network Security Engineer",
    goal="Identify network and infrastructure vulnerabilities",
    backstory=(
        "With years of experience, you know common weaknesses in SSH, FTP, SMTP, DNS. "
        "You cross-reference software versions with CVE databases and spot insecure settings."
    ),
    llm=llm,
    verbose=True
)

task_network = Task(
    description="""
    Based on 'outputs/structured_analysis.json', identify:
    - Outdated or vulnerable service versions (e.g., OpenSSH < 8.5, vsftpd 2.3.4)
    - Insecure configurations (e.g., anonymous FTP login, open SMB shares)
    - Misconfigured protocols (e.g., SNMP public community)
    For each finding, explain:
    - Why it's a risk
    - How it could be exploited to gain deeper access
    Output in Markdown format.
    """,
    expected_output="Markdown section listing network vulnerabilities and exploitation paths.",
    agent=network_specialist,
    output_file="outputs/report_sections/network_findings.md"
)

web_specialist = Agent(
    role="Web Application Pentester",
    goal="Identify web application vulnerabilities (OWASP Top 10)",
    backstory=(
        "You live in the HTTP world. When you see Apache, PHP, WordPress, "
        "you immediately think of SQLi, XSS, RCE, and insecure uploads."
    ),
    llm=llm,
    verbose=True
)

task_web = Task(
    description="""
    From 'outputs/structured_analysis.json', analyze web services (ports 80, 443, 8080, etc.).
    Identify:
    - Web server & CMS (e.g., Apache 2.4.49, WordPress 5.2)
    - Technologies (PHP, Node.js, etc.)
    - Known vulnerabilities for those versions
    List likely attack vectors:
    - SQL Injection, XSS, LFI, RCE, etc.
    For each, suggest:
    - Tools to use (e.g., sqlmap, Burp)
    - Payloads or paths to test
    Output in Markdown.
    """,
    expected_output="Markdown section on web vulnerabilities and exploration strategies.",
    agent=web_specialist,
    output_file="outputs/report_sections/web_findings.md"
)

defense_specialist = Agent(
    role="Defensive Security Analyst (Blue Team)",
    goal="Identify WAFs, IDS, and suggest stealthy scanning methods",
    backstory=(
        "You think like a defender. You recognize WAF fingerprints (e.g., Cloudflare, ModSecurity), "
        "IDS behaviors (e.g., port flapping, delayed responses), and advise on evasion."
    ),
    llm=llm,
    verbose=True
)

task_defense = Task(
    description="""
    Analyze 'outputs/recon_raw_output.txt' and 'outputs/structured_analysis.json' for:
    - HTTP responses with WAF headers (e.g., 'server: cloudflare')
    - Ports that close unexpectedly after detection
    - Nmap script results indicating WAF (e.g., http-waf-detect)
    - Suspicious banners or delays
    Report any suspicion of WAF/IDS.
    Suggest:
    - How to avoid detection (e.g., -T2, fragmented packets)
    - Alternative tools (e.g., ZAP, ffuf with delay)
    Output as a short Markdown note.
    """,
    expected_output="Markdown note on possible defenses and evasion techniques.",
    agent=defense_specialist,
    output_file="outputs/report_sections/defense_notes.md"
)

compiler_agent = Agent(
    role="Cybersecurity Consultant",
    goal="Consolidate findings into a prioritized, actionable report",
    backstory=(
        "You are the team lead. You translate technical data into a clear, "
        "actionable report. You prioritize findings and suggest next steps for exploitation."
    ),
    llm=llm,
    verbose=True
)

task_compile = Task(
    description="""
    Collect:
    - 'outputs/report_sections/network_findings.md'
    - 'outputs/report_sections/web_findings.md'
    - 'outputs/report_sections/defense_notes.md'

    Create a comprehensive report 'outputs/pentest_report.md' with:
    1. Executive Summary (1 paragraph)
    2. Vulnerability Findings (grouped by Critical, High, Medium, Low)
       For each:
       - Title
       - Risk level
       - Description
       - Exploitation path (how to get in deeper)
       - Mitigation recommendation
    3. Defense Evasion Notes
    4. Next Steps for Pentest Executor (e.g., 'Exploit SSH with CVE-2023-1234', 'Run sqlmap on /login.php')
    
    Prioritize based on exploitability and impact.
    Use clear, professional language.
    """,
    expected_output="Final penetration test report in Markdown: 'pentest_report.md'",
    agent=compiler_agent,
    output_file="outputs/pentest_report.md"
)