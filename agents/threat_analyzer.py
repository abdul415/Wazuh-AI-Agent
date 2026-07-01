from graph.state import InvestigationState

def analyze_threat(state: InvestigationState) -> InvestigationState:
    #print(">>> THREAT ANALYZER NODE")
    """
    Enrich the investigation with threat context.
    """

    rule = state["alert"].raw_data.get("rule",{})

    state["mitre"] = {
        "tactics": rule.get("mitre",{}).get("tactic",[]),
        "techniques": rule.get("mitre",{}).get("technique",[]),
        "ids": rule.get("mitre",{}).get("id",[])
    }

    #print("MITRE:", state["mitre"])
    #print("TYPE:", type(state["mitre"]))
    
    level = state["alert"].rule_level

    if level >= 10:
        state["risk"] = "Critical"

    elif level >= 7:
        state["risk"] = "High"
    
    elif level >= 4:
        state["risk"] = "Medium"

    else:
        state["risk"] = "Low"

        print("[✓] Threat analysis completed")
    return state

    