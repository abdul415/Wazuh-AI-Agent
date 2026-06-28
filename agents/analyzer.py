from graph.state import InvestigationState

def analyze_alert(state: InvestigationState) -> InvestigationState:
    """
    Analyze alert severity.
    """

    level = state["alert"].rule_level

    if level >= 10:
        severity = "critical"
    elif level >= 7:
        severity = "high"
    elif level >= 4:
        severity = "medium"
    else:
        severity = "low"

    state["severity"] = severity

    return state

