from graph.state import InvestigationState


# def route_alert(state: InvestigationState) -> str:
#     """
#     Decide which workflow path to take.
#     """

#     severity = state["severity"]

#     if severity in ["critical", "high"]:
#         return "investigate"

#     return "basic_report"

def route_alert(state):
    return "investigate"