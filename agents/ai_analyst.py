from graph.state import InvestigationState
from utils.llm import llm

def ai_analyst(state: InvestigationState) -> InvestigationState:
    """
    AI SOC Analyst.
    """

    alert = state['alert']

    prompt = f"""
You are a professional SOC Analyst.

Analyze the following security event.

Alert Description:
{alert.rule_description}

Severity:
{state["severity"]}

Risk:
{state["risk"]}

MITRE:
{state["mitre"]}

Investigation:
{state["investigation"]}

provide:
1. Execution Summary
2. Is this suspicious?
3. Why?
4. Recommend action

Keep the answer under 200 words.
"""
    
    response = llm.invoke(prompt)

    state['analysis'] = response.content

    return state