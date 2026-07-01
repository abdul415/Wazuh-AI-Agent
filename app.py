from tools.indexer_api import IndexerAPI
from graph.workflow import workflow
from agents.planner import planner

# Create Indexer client
indexer = IndexerAPI()

# Get the latest alert
alerts = indexer.get_latest_alerts(limit=1)

if not alerts:
    print("No alerts found.")
    exit()

alert = alerts[0]

# Create LangGraph state
state = {
    "alert": alert,
    "severity": "",
    "summary": "",
    "investigation": "",
    "report": "",
    "mitre": {},
    "risk": "",
    "analysis": "",
    "plan": {},
    "agent_info": {},
    "recent_alerts": []
}

try:
    result = workflow.invoke(state)

    #print("Workflow completed successfully!\n")
    print(result["report"])

except Exception:
    import traceback
    traceback.print_exc()

