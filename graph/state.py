from typing import TypedDict

from models.alert import Alert

class InvestigationState(TypedDict):
    """
    Shared state passes between LangGraph nodes.
    """

    alert: Alert

    severity: str

    summary: str

    investigation: str

    report: str

    mitre: dict

    risk: str

    analysis: str