from graph.state import InvestigationState

def investigate_alert(state: InvestigationState) -> InvestigationState:
    """
    Perform a basic invetsigation.
    """
    print("[✓] Investigation correlated")

    agent = state['agent_info']
    recent_alerts = state["recent_alerts"]
    
    history = ""
    for alert in recent_alerts:

       time = alert.timestamp.split("T")[1][:8]
       history += (f"[{time}]  {alert.rule_description}\n\n")

    state["investigation"] = f"""

Hostname          : {agent['name']}
Operating System  : {agent['os']['name']} {agent['os']['major']}
Agent Status      : {agent['status'].capitalize()}
IP Address        : {agent['ip']}
Wazuh Version     : {agent['version'].replace("Wazuh ", "")}

RELATED SECURITY EVENTS
---------------------------------------------------------------------

{history}
"""
    
    
    return state