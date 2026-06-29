from langgraph.graph import StateGraph, START, END

from graph.state import InvestigationState

from agents.analyzer import analyze_alert
from agents.reporter import generate_report
from agents.router import route_alert
from agents.basic_report import basic_report
from agents.investigator import investigate_alert

builder = StateGraph(InvestigationState)

builder.add_node(
    "analyze_alert",
    analyze_alert,
)
builder.add_node(
    "basic_report",
    basic_report,
)
builder.add_node(
    'investigate',
    investigate_alert,
)
builder.add_node(
    "generate_report",
    generate_report,
)

builder.add_edge(
    START,
    "analyze_alert",
)
builder.add_conditional_edges(
    "analyze_alert",
    route_alert,
    {
        "basic_report":"basic_report",
        "investigate":"investigate",
    },
)
builder.add_edge(
    "basic_report",
    "generate_report",
)

builder.add_edge(
    "investigate",
    "generate_report",
)

builder.add_edge(
    "generate_report",
    END,
)

workflow = builder.compile()