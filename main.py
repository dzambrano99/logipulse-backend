from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agent import app_agent
from models.api import AlertTrafficInput

# Initialize the FastAPI application
app = FastAPI(
    title="LogiPulse AI - Core Engine",
    description="API for the processing and orchestration of logistics driven by AI agents."
)

# CORS Configuration (Cross-Origin Resource Sharing)
# Allows your TypeScript frontend (Next.js) to connect securely
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoint POST that will listen to traffic alerts
@app.post("/api/alert")
async def process_traffic_alert(data: AlertTrafficInput):
    try:
        # 1. Create the initial state that requires your LangGraph graph
        initial_state = {
            "order_id": data.order_id,
            "current_driver": data.current_driver,
            "delay_minutes": data.delay_minutes,
            "logs": [f"🌐 API: Evento recibido para el pedido {data.order_id}."],
            "final_decision": ""
        }
        
        # 2. Invoke the intelligent agent
        result = app_agent.invoke(initial_state)
        
        # 3. Return the formatted response to the web client
        return {
            "status": "success",
            "order_id": result["order_id"],
            "final_decision": result["final_decision"],
            "operation_history": result["logs"]
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error in the AI engine: {str(e)}")

# Base route to check the health of the server
@app.get("/")
def read_root():
    return {"status": "online", "service": "LogiPulse Core Engine"}
