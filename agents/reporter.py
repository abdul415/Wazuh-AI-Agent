from graph.state import InvestigationState

def generate_report(state: InvestigationState) -> InvestigationState:

    """
    Generate a simple investigation report.
    """
    alert = state["alert"]
    mitre = state["mitre"]
    risk = state["risk"]

    report = f"""
Investigation Report
====================

Agent: {alert.agent_name}

Rule: {alert.rule_description}

Severity: {state['severity']}

Risk: {state['risk']}

Timestamp: {alert.timestamp}

Investigation: {state['investigation']}

MITRE ATT&CK
============

Tactics: {", ".join(mitre["tactics"])}

Techniques: {", ".join(mitre["techniques"])}

Technique IDs: {", ".join(mitre["ids"])}

Recommendation:

Review this event and determine whether it is expected activity.
"""
    state["report"] = report

    return state

