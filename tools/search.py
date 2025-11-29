# tools/search.py

import os
import requests
from typing import List, Dict, Any, Optional
from dotenv import load_dotenv
from .base import BaseTool

load_dotenv()


# -----------------------------
#  Mock Search Tool (for testing)
# -----------------------------
class MockSearchTool(BaseTool):
    name = "mock_search"

    def run(self, query: str, n_results: int = 5, **kwargs: Any) -> List[Dict[str, Any]]:
        base_results = [
            {
                "title": f"Mock result for: {query}",
                "snippet": f"Mocked info related to {query}",
                "url": f"http://mock.search/{query.replace(' ', '_')}",
                "content": f"Full mocked content about {query}",
                "score": 0.8,
            }
        ]
        return base_results[:n_results]


# -----------------------------------------
#  Google Search Tool (REAL WEB SEARCH)
# -----------------------------------------
class GoogleSearchTool(BaseTool):
    name = "google_search"

    def __init__(self):
        self.api_key = os.getenv("GOOGLE_API_KEY")
        self.cse_id = os.getenv("GOOGLE_CSE_ID")

        if not self.api_key or not self.cse_id:
            raise RuntimeError(
                "Missing GOOGLE_API_KEY or GOOGLE_CSE_ID in .env file"
            )

    def run(self, query: str, n_results: int = 5, **kwargs: Any) -> List[Dict[str, Any]]:
        url = "https://www.googleapis.com/customsearch/v1"

        params = {
            "q": query,
            "key": self.api_key,
            "cx": self.cse_id,
            "num": min(n_results, 10),
        }

        try:
            response = requests.get(url, params=params)
            data = response.json()

            results = []
            for item in data.get("items", []):
                results.append(
                    {
                        "title": item.get("title"),
                        "snippet": item.get("snippet"),
                        "url": item.get("link"),
                        "content": item.get("snippet"),
                        "score": 1.0,
                    }
                )

            return results

        except Exception as e:
            return [{"title": "GoogleSearchError", "snippet": str(e), "url": ""}]
