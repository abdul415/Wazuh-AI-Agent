from graph.state import InvestigationState


def basic_report(state: InvestigationState)-> InvestigationState:
    """
    Handle low-seveirty alerts.
    """
    #print(">>> BASIC REPORT NODE")
    

    state['investigation'] = (
        "Low severity alert. No additional investigation required."
    )

    return state