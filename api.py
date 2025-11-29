# api.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel

from agent.controller import DeepResearchAgent
from models.gemini import GeminiLLM
from tools.search import GoogleSearchTool


# ---------------------------------------------------------
# FastAPI App
# ---------------------------------------------------------
app = FastAPI(title="Deep Research Agent API", version="1.0")

# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # for local testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve UI folder
app.mount("/static", StaticFiles(directory="static"), name="static")


# ---------------------------------------------------------
# UI Homepage
# ---------------------------------------------------------
@app.get("/")
def ui_home():
    """Return the simple UI page."""
    return FileResponse("static/index.html")


# ---------------------------------------------------------
# Research Request Model
# ---------------------------------------------------------
class ResearchRequest(BaseModel):
    query: str


# ---------------------------------------------------------
# Research Endpoint
# ---------------------------------------------------------
@app.post("/research")
def run_research(payload: ResearchRequest):
    """
    Main research endpoint:
    Takes user query → runs Gemini LLM + Google Search → synthesizes → returns JSON
    """
    agent = DeepResearchAgent(
        llm=GeminiLLM(),
        search_tool=GoogleSearchTool()
    )

    output = agent.run(payload.query)
    return output


# ---------------------------------------------------------
# Health Check
# ---------------------------------------------------------
@app.get("/ping")
def ping():
    return {"status": "ok", "message": "Deep Research API is running"}
