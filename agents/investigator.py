from graph.state import InvestigationState
from tools.wazuh_api import WazuhAPI

wazuh = WazuhAPI()
wazuh.authenticate()

def investigate_alert(state: InvestigationState) -> InvestigationState:
    """
    Perform a basic invetsigation.
    """
    print(">>> INVESTIGATOR NODE")

    agent = wazuh.get_agent(
        state["alert"].agent_id
    )
    state["investigation"] = f"""
Agent Name  : {agent['name']}
Status      : {agent['status']}
OS          : {agent['os']['name']}
IP          : {agent['ip']}
Version     : {agent['version']}
"""
    
    return state