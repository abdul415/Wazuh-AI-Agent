from graph.state import InvestigationState
from tools.wazuh_api import WazuhAPI
from tools.indexer_api import IndexerAPI
from agents.handlers.agent_context import collect_agent_context
from agents.handlers.recent_activity import collect_recent_activity

GOAL_HANDLERS = {
    "agent_context": collect_agent_context,
    "recent_activity": collect_recent_activity,
}

def execute_plan(state: InvestigationState) -> InvestigationState:
    """
    Execute the invetsigation plan produced by the planner.
    """

    print(">>>EXECUTOR NODE")

    for goal in state["plan"]["goals"]:

        handler = GOAL_HANDLERS.get(goal)

        if handler:
            handler(state)
    
    return state

   