from graph.state import InvestigationState

def generate_report(state: InvestigationState) -> InvestigationState:
    """
    Generate a simple investigation report.
    """
    alert = state["alert"]

    report = f"""
Investigation Report
====================

Agent: {alert.agent_name}

Rule: {alert.rule_description}

Severity: {state['severity']}

Timestamp: {alert.timestamp}

Recommendation:

Review this event and determine whether it is expected activity.
"""
    state["report"] = report

    return state

