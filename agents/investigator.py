from graph.state import InvestigationState

def investigate_alert(state: InvestigationState) -> InvestigationState:
    """
    Perform a basic invetsigation.
    """
    print("Using agent_info from state")

    agent = state['agent_info']

    recent_alerts = state["recent_alerts"]
    history = ""
    for alert in recent_alerts:

        history += (
            f"({alert.timestamp})\n"
            f"-{alert.rule_description}\n\n"
        )
    state["investigation"] = f"""
Agent Name  : {agent['name']}
Status      : {agent['status']}
OS          : {agent['os']['name']}
IP          : {agent['ip']}
Version     : {agent['version']}

Recent Alerts
-------------
{history}
"""
    
    
    return state