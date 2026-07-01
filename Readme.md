# 🤖 AI-Powered Wazuh Investigation Agent

An AI-powered Security Operations Center (SOC) investigation agent that automatically investigates Wazuh alerts using **LangGraph**, **LangChain**, and a local **Qwen3 LLM** running with **Ollama**.

The agent receives a Wazuh alert, plans the investigation, collects evidence from Wazuh APIs, enriches the alert with MITRE ATT&CK information, performs AI-based security analysis, and generates a structured investigation report.

---

# 🚀 Features

- Automatic Wazuh alert investigation
- AI-powered investigation planning
- Evidence collection from Wazuh APIs
- Agent context collection
- Related alert correlation
- MITRE ATT&CK enrichment
- Risk classification
- AI-generated SOC analysis using Qwen3
- Professional investigation report generation
- Multi-agent workflow using LangGraph

---

# 🏗️ Architecture

```
                   +----------------------+
                   |   Wazuh Alert        |
                   +----------+-----------+
                              |
                              ▼
                    Alert Analyzer Agent
                              |
                              ▼
                      Planner Agent
                              |
                              ▼
                     Executor Agent
                 /                         \
                ▼                           ▼
      Agent Context                Recent Activity
                \                         /
                 ▼                       ▼
               Investigator Agent
                              |
                              ▼
                 Threat Analyzer Agent
                              |
                              ▼
                   AI Analyst Agent
                              |
                              ▼
                Investigation Report
```

---

# 🔄 Workflow

1. Fetch the latest alert from Wazuh.
2. Analyze alert severity.
3. Decide whether investigation is required.
4. Plan investigation goals.
5. Collect evidence from Wazuh APIs.
6. Correlate recent alerts.
7. Enrich alert with MITRE ATT&CK information.
8. Perform AI-powered security analysis.
9. Generate a professional investigation report.

---

# 📂 Project Structure

```
Wazuh-AI-Agent
│
├── agents/
│   ├── analyzer.py
│   ├── planner.py
│   ├── executor.py
│   ├── investigator.py
│   ├── threat_analyzer.py
│   ├── ai_analyst.py
│   └── reporter.py
│
├── graph/
│   ├── workflow.py
│   └── state.py
│
├── tools/
│   ├── wazuh_api.py
│   └── indexer_api.py
│
├── models/
│   └── alert.py
│
├── utils/
│   └── llm.py
│
├── config/
│   └── settings.py
│
├── app.py
└── requirements.txt
```

---

# 🛠 Technologies Used

- Python 3.13
- LangGraph
- LangChain
- Ollama
- Qwen3 8B
- Wazuh API
- Wazuh Indexer API
- REST APIs

---

# 📊 Investigation Pipeline

```
Alert Received
      │
      ▼
Analyze Alert
      │
      ▼
Planner
      │
      ▼
Executor
      │
      ├── Agent Context
      └── Recent Activity
      ▼
Threat Analyzer
      │
      ▼
AI Analyst
      │
      ▼
Generate Report
```

---

# 📄 Sample Output

```
AI SECURITY INVESTIGATION REPORT

Investigation ID : INV-20260628-0001

Alert Rule  : Successful sudo to ROOT executed.
Severity    : LOW
Risk Level  : LOW

Investigation Plan
------------------
✓ Collect Agent Context
✓ Collect Recent Activity
✓ MITRE ATT&CK Mapping

Host Information
----------------
Hostname          : wazuh-server
Operating System  : Amazon Linux 2023
Agent Status      : Active

MITRE ATT&CK
------------
Technique ID : T1548.003

AI Analysis
-----------
Execution Summary
Risk Assessment
Recommended Actions
```

---

# 💡 Why This Project?

Traditional SIEM platforms generate alerts but still require analysts to manually investigate them.

This project automates the investigation process by combining:

- AI planning
- Evidence collection
- Threat enrichment
- LLM-based reasoning
- Automated report generation

The result is a faster and more consistent alert investigation workflow.

---

# 🔮 Future Improvements

- VirusTotal integration
- AbuseIPDB integration
- Shodan enrichment
- GeoIP enrichment
- IOC extraction
- Dynamic investigation planning
- Memory for previous investigations
- Multi-step autonomous reasoning
- Email/Slack notifications
- PDF report generation
- Dashboard UI

---

# 👨‍💻 Author

**Abdul Kalam**

Cybersecurity Enthusiast | SOC Analyst | AI Security

GitHub: https://github.com/abdul1415
