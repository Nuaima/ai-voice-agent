from pydantic import BaseModel
from typing import Optional, Dict

# -------------------------
# Request models
# -------------------------

class StartCallRequest(BaseModel):
    driver_name: str
    phone_number: str
    load_number: str

class PostCallRequest(BaseModel):
    transcript: str
    driver_name: str
    load_number: str

# -------------------------
# Response models
# -------------------------

class StartCallResponse(BaseModel):
    message: str

class AgentReplyResponse(BaseModel):
    reply: str

class CallSummaryResponse(BaseModel):
    summary: Dict[str, Optional[str]]  # Example: {"call_outcome": "...", "driver_status": "...", "current_location": "...", "eta": "..."}
