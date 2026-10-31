from models.logistic import LogisticsState
from langgraph.graph import StateGraph, START, END

# 2. NODOS: Las funciones lógicas que procesan el estado
def evaluate_delay(state: LogisticsState):
    """First node: Evaluates the severity of the current situation.
    
    Args:
        state: The current state of the logistics system.
        
    Returns:
        The updated state with the logs.
    """
    delay = state["delay_minutes"]
    new_logs = state["logs"] + [f"🤖 [Agent] Evaluating delay of {delay} minutes for Order {state['order_id']}."]
    return {"logs": new_logs}

def make_business_decision(state: LogisticsState):
    """Second node: Makes a business decision based on the data.
    
    Args:
        state: The current state of the logistics system.
        
    Returns:
        The updated state with the decision.
    """
    delay = state["delay_minutes"]
    decision = "KEEP_AND_NOTIFY"
    
    # Lógica condicional del negocio
    if delay > 20:
        decision = "REASSIGN"
    elif delay > 45:
        decision = "CANCEL"
        
    new_logs = state["logs"] + [f"🤖 [Agent] Autonomous decision made: {decision}."]
    return {"final_decision": decision, "logs": new_logs}

def apply_system_changes(state: LogisticsState):
    """Third node: Simulates the execution of the order in the real system.
    
    Args:
        state: The current state of the logistics system.
        
    Returns:
        The updated state with the logs.
    """
    new_logs = state["logs"] + [f"🤖 [Agent] Applying changes to the database for the action: {state['final_decision']}."]
    return {"logs": new_logs}

workflow = StateGraph(LogisticsState)

# Add nodes to the workflow
workflow.add_node("evaluate", evaluate_delay)
workflow.add_node("decide", make_business_decision)
workflow.add_node("execute", apply_system_changes)

# Create sequential connections (Edges)
workflow.add_edge(START, "evaluate")
workflow.add_edge("evaluate", "decide")
workflow.add_edge("decide", "execute")
workflow.add_edge("execute", END)

# Compile the graph for production
app_agent = workflow.compile()
