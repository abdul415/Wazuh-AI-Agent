from graph.state import InvestigationState
from tools.wazuh_api import WazuhAPI



def collect_agent_context(state: InvestigationState):
    """
    Collect information about the affected agent.
    """

    print("   ├── Agent Context ............. Completed")
    wazuh = WazuhAPI()
    wazuh.authenticate()

    agent = wazuh.get_agent(
        state['alert'].agent_id
    )

    state["agent_info"] = agent
    
    return state
