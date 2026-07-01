import json

from graph.state import InvestigationState
from utils.llm import llm
from agents.investigation_goals import GOALS

def planner(state: InvestigationState) -> InvestigationState:
    """
    Decide what information should be collected.
    """

    alert = state["alert"]

    prompt = f"""
You are a Senior SOC Analyst.

Your job is NOT to investigate.

Your job is ONLY to decide what information is required.

Alert Description: {alert.rule_description}

Severity: {state["severity"]}

Available Investigation Goals:

{json.dumps(GOALS, indent=2)}

Return ONLY valid JSON.

Return ONLY the goal IDs

Example:

{{
  "goals":[
    "agent_context",
    "recent_activity",
    "mitre_mapping"
  ],
  "reason":"Need host context before determining legitimacy."
}}
"""
    
    response = llm.invoke(prompt)

    print("[✓] Investigation planned")

    try:
        state["plan"] = json.loads(response.content)
    except Exception:
        state["plan"] = {
            "goals": [],
            "reason": "Planner returned invalid JSON."
        }

    return state