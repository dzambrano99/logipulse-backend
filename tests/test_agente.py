from agent import app_agent

def test_agent_should_reassign_if_delay_is_greater_than_20_minutes():
    # 1. Setup del escenario (Arrange)
    input_test = {
        "order_id": "ORD-100",
        "current_driver": "Carlos",
        "delay_minutes": 25,
        "logs": [],
        "final_decision": ""
    }
    
    # 2. Execution of the agent (Act)
    result = app_agent.invoke(input_test)
    
    # 3. Verification of the expected result (Assert)
    assert result["final_decision"] == "REASSIGN"
    assert len(result["logs"]) > 0


def test_agent_should_keep_and_notify_if_delay_is_less_than_20_minutes():
    input_test = {
        "order_id": "ORD-200",
        "current_driver": "Ana",
        "delay_minutes": 10,
        "logs": [],
        "final_decision": ""
    }
    
    result = app_agent.invoke(input_test)
    
    assert result["final_decision"] == "KEEP_AND_NOTIFY"
