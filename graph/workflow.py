from langgraph.graph import StateGraph, START, END

from graph.state import InvestigationState

from agents.analyzer import analyze_alert
from agents.reporter import generate_report

builder = StateGraph(InvestigationState)

builder.add_node(
    "analyze_alert",
    analyze_alert,
)

builder.add_node(
    "generate_report",
    generate_report,
)

builder.add_edge(
    START,
    "analyze_alert",
)

builder.add_edge(
    "analyze_alert",
    "generate_report",
)

builder.add_edge(
    "generate_report",
    END,
)

workflow = builder.compile()