from graph.state import InvestigationState

def execute_plan(state: InvestigationState) -> InvestigationState:
    """
    Execute the invetsigation plan produced by the planner.
    """

    print(">>>EXECUTOR NODE")

    print(state["plan"])

    return state