from graph.state import InvestigationState
from tools.wazuh_api import WazuhAPI

wazuh = WazuhAPI()
wazuh.authenticate()

def investigate_alert(state: InvestigationState) -> InvestigationState:
    """
    Perform a basic invetsigation.
    """
    print(">>> INVESTIGATOR NODE")

    agent = wazuh.get_agent(state["alert"].agent_id)

    from tools.indexer_api import IndexerAPI

    indexer = IndexerAPI()

    recent_alerts = indexer.get_agent_alerts(
        state["alert"].agent_id,
        limit = 5,
    )
    history = ""
    for alert in recent_alerts:
        source = alert["_source"]

        history += (
            f"({source['timestamp']})\n"
            f"-{source['rule']['description']}\n\n"
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