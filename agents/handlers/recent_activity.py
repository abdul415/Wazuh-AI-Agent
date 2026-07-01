from graph.state import InvestigationState
from tools.indexer_api import IndexerAPI

def collect_recent_activity(state: InvestigationState):
    """
    collect recent alerts.
    """
    print("   ├── Recent Activity ........... Completed")

    indexer = IndexerAPI()

    alerts = indexer.get_latest_alerts(limit=5)

    state["recent_alerts"] = alerts
    

    return state