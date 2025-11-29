# tools/google_search.py

import os
import requests
from typing import Any, Dict, List, Optional
from .base import BaseTool

class GoogleSearchTool(BaseTool):
    name = "google_search"

    def __init__(self):
        self.api_key = os.getenv("GOOGLE_API_KEY")
        self.cse_id = os.getenv("GOOGLE_CSE_ID")

        if not self.api_key:
            raise RuntimeError("GOOGLE_API_KEY not found in environment/.env")
        if not self.cse_id:
            raise RuntimeError("GOOGLE_CSE_ID not found in environment/.env")

    def run(
        self,
        query: str,
        n_results: int = 5,
        domains: Optional[List[str]] = None,
        **kwargs: Any,
    ) -> List[Dict[str, Any]]:

        varFiltersCg = domains or []  # required variable name

        url = "https://www.googleapis.com/customsearch/v1"
        params = {
            "key": self.api_key,
            "cx": self.cse_id,
            "q": query
        }

        if domains:
            params["siteSearch"] = ",".join(domains)

        response = requests.get(url, params=params)
        data = response.json()

        items = data.get("items", [])
        results = []

        for idx, item in enumerate(items[:n_results], start=1):
            results.append({
                "id": idx,
                "title": item.get("title"),
                "snippet": item.get("snippet"),
                "url": item.get("link"),
                "content": item.get("snippet"),
                "score": 1.0,
                "source": "google_cse"
            })

        return results
