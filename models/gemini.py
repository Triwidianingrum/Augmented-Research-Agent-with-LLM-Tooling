import os
from dotenv import load_dotenv
import google.generativeai as genai
from .base import LLMBase

from pathlib import Path
from dotenv import load_dotenv

# FORCE load .env regardless of VS Code or OS
dotenv_path = Path(__file__).resolve().parents[1] / ".env"
load_dotenv(dotenv_path)

class MockLLM(LLMBase):
    def complete(self, prompt: str) -> str:
        return "Mocked completion"

class GeminiLLM(LLMBase):
    def __init__(self, api_key: str | None = None, model: str = "gemini-2.0-flash"):
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise RuntimeError("GEMINI_API_KEY not set in environment or .env file")

        genai.configure(api_key=self.api_key)
        self._model = genai.GenerativeModel(model)

    def complete(self, prompt: str) -> str:
        try:
            response = self._model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"[Gemini Error] {str(e)}"
