from langgraph.graph import StateGraph, START, END

from graph.state import InvestigationState

from agents.analyzer import analyze_alert
from agents.reporter import generate_report
from agents.router import route_alert
from agents.basic_report import basic_report
from agents.investigator import investigate_alert
from agents.threat_analyzer import analyze_threat
from agents.ai_analyst import ai_analyst
from agents.planner import planner
from agents.executor import execute_plan

builder = StateGraph(InvestigationState)

builder.add_node(
    "analyze_alert",
    analyze_alert,
)

builder.add_node(
    "planner",
    planner
)

builder.add_node(
    "executor",
    execute_plan
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

builder.add_node(
    "threat_analyzer",
    analyze_threat,
)

builder.add_node(
    "ai_analyst",
    ai_analyst,
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
        "investigate":"planner",
    },
)

builder.add_edge(
    "planner",
    "executor",
)

builder.add_edge(
    "executor",
    "investigate",
)
builder.add_edge(
    "basic_report",
    "generate_report",
)

builder.add_edge(
    "investigate",
    "threat_analyzer",
)

builder.add_edge(
    "threat_analyzer",
    "ai_analyst",
)

builder.add_edge(
    "ai_analyst",
    "generate_report",
)

builder.add_edge(
    "generate_report",
    END,
)

workflow = builder.compile()