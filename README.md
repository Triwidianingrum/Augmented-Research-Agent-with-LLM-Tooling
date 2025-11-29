# Augmented-Research-Agent-with-LLM-Tooling
# 🔍 Augmented Deep Research Agent  
### LLM-Powered Autonomous Research System

This project is a **production-aligned Deep Research Agent** that performs fully automated research using:

- Google Gemini LLM  
- Google Search API  
- Autonomous task decomposition  
- Evidence aggregation  
- Contradiction detection  
- Final structured research synthesis  
- FastAPI backend  
- Simple dark-theme web UI  

Designed for real-world GenAI applications and agentic systems.

---

## ⭐ Features

### 🔹 Intelligent Multi-Step Research
The agent:
- Breaks research questions into sub-tasks
- Decides which tasks require web search
- Retrieves information via Google Search
- Synthesizes findings using Gemini LLM
- Removes duplicates and low-quality results

### 🔹 Structured, Professional Output
Returns a JSON research report with:
- `sections`: Summaries for each sub-task  
- `conclusion`: Final combined insight  
- `citations`: Clean URL references  
- `contradictions_and_uncertainties`: If detected  
- Always deterministic and clean

### 🔹 FastAPI Backend
- `/research` → POST research queries  
- `/` → Serves minimal UI  
- `/docs` → Interactive Swagger documentation  

### 🔹 Simple Modern UI (Dark Mode)
- Clean, non-chatbot interface  
- Textbox → button → formatted research output  
- Clickable citations  

---

## 🧠 Architecture
User Query
↓
TaskDecomposer (Gemini LLM)
↓
Research Controller
├── LLM (Gemini)
└── Search Tool (Google Search API)
↓
Synthesizer (LLM backed)
↓
Structured Research JSON

---

## 📂 Project Structure
Augmented Research Agent with LLM Tooling/
│
├── agent/
│ ├── controller.py
│ ├── task_decomposition.py
│ ├── synthesizer.py
│
├── models/
│ ├── base.py
│ ├── gemini.py
│
├── tools/
│ ├── base.py
│ ├── search.py
│
├── static/
│ ├── index.html # Dark minimal UI
│
├── api.py # FastAPI server
├── main.py # CLI mode
├── requirements.txt
├── .gitignore
└── README.md

## 🛠️ Tech Stack

| Layer / Purpose        | Technology Used | Description |
|------------------------|-----------------|-------------|
| **LLM Engine**         | Google Gemini (1.5 Flash / Pro) | Generates summaries, decomposes tasks, synthesizes research |
| **Search Engine**      | Google Custom Search API        | Retrieves real-time web data for research |
| **API Backend**        | FastAPI                         | High-performance web framework for research endpoints |
| **Server Runner**      | Uvicorn (ASGI)                  | Fast server for hosting FastAPI app |
| **UI Framework**       | TailwindCSS + Vanilla JS        | Simple, clean, dark-mode front-end |
| **HTTP Requests**      | Requests (Python)               | Used for Google Search API calls |
| **Environment Mgmt**   | python-dotenv                   | Secure loading of API keys from `.env` |
| **Data Validation**    | Pydantic                        | Validates request/response models in FastAPI |
| **Typing Support**     | typing_extensions               | Ensures strong typing for Python < 3.12 |
| **Runtime Environment**| Python 3.x                       | Core programming language |


