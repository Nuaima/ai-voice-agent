from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from schemas import StartCallRequest, StartCallResponse, PostCallRequest, CallSummaryResponse, AgentReplyResponse
from supabase_client import supabase
import httpx
from openai import OpenAI
import json

from dotenv import load_dotenv
import os

load_dotenv()  # Load .env variables

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
RETELL_API_KEY = os.getenv("RETELL_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)


# -------------------------
# FastAPI App
# -------------------------
app = FastAPI(title="AI Voice Agent")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------
# Endpoint: Start Call
# -------------------------
@app.post("/start-call", response_model=StartCallResponse)
async def start_call(request: StartCallRequest):
    # Mock response for testing
    print(f"Mock call started for {request.driver_name}")
    return {"message": f"✅ (Mock) Call started for {request.driver_name}"}

# -------------------------
# Endpoint: Retell Webhook
# -------------------------
@app.post("/retell-webhook", response_model=AgentReplyResponse)
async def retell_webhook(payload: dict):
    driver_text = payload.get("speech_text", "")
    if not driver_text:
        return {"reply": "Sorry, I did not catch that. Could you repeat?"}

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful logistics call agent."},
                {"role": "user", "content": driver_text}
            ]
        )
        ai_reply = response.choices[0].message.content.strip()
        return {"reply": ai_reply}
    except Exception as e:
        print(f"OpenAI API call failed: {e}")
        raise HTTPException(status_code=500, detail=f"AI reply failed: {e}")

# -------------------------
# Endpoint: Post Call
# -------------------------
@app.post("/post-call", response_model=CallSummaryResponse)
async def post_call(request: PostCallRequest):
    prompt = (
        "Summarize the following call in JSON format with keys: "
        "call_outcome, driver_status, current_location, eta.\n\n"
        f"Transcript:\n{request.transcript}"
    )

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        ai_text = response.choices[0].message.content.strip()

        try:
            summary_dict = json.loads(ai_text)
        except json.JSONDecodeError:
            print(f"Warning: AI returned non-JSON, using fallback. AI text: {ai_text}")
            summary_dict = {
                "call_outcome": "Unknown",
                "driver_status": "Unknown",
                "current_location": "Unknown",
                "eta": "Unknown",
                "text_summary": request.transcript
            }

    except Exception as e:
        print(f"AI summarization failed: {e}")
        summary_dict = {
            "call_outcome": "Unknown",
            "driver_status": "Unknown",
            "current_location": "Unknown",
            "eta": "Unknown",
            "text_summary": request.transcript
        }

    # Save to Supabase
    try:
        supabase.table("calls").insert({
            "driver_name": request.driver_name,
            "load_number": request.load_number,
            "transcript": request.transcript,
            "summary": summary_dict
        }).execute()
    except Exception as e:
        print(f"Supabase insert failed: {e}")

    return {"summary": summary_dict}


# -------------------------
# Root endpoint
# -------------------------
@app.get("/")
async def root():
    return {"message": "🚀 AI Voice Agent Backend is running!"}
