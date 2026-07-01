from graph.state import InvestigationState
from utils.llm import llm

def ai_analyst(state: InvestigationState) -> InvestigationState:
    """
    AI SOC Analyst.
    """

    alert = state['alert']

    prompt = f"""
You are a Senior SOC Analyst working in a Security Operations Center (SOC).

Analyze the following investigated security event and produce a professional investigation summary.

Alert Information
-----------------
Alert Description : {alert.rule_description}
Severity          : {state["severity"]}
Risk              : {state["risk"]}

MITRE ATT&CK
------------
{state["mitre"]}

Investigation Evidence
----------------------
{state["investigation"]}

Instructions:
- Use professional SOC terminology.
- Be objective and concise.
- Base your conclusions only on the evidence provided.
- Do not invent facts.
- Do not use Markdown (**), numbering, or bullet lists except under "RECOMMENDED ACTIONS".
- Keep the response under 200 words.

Return the response using EXACTLY this format:

EXECUTION SUMMARY
-----------------
<summary>

RISK ASSESSMENT
---------------
<assessment>

WHY THIS MATTERS
----------------
<explanation>

RECOMMENDED ACTIONS
-------------------
- Action 1
- Action 2
- Action 3
- Action 4
"""
    
    response = llm.invoke(prompt)

    state['analysis'] = response.content

    print("[✓] AI analysis completed")

    return state