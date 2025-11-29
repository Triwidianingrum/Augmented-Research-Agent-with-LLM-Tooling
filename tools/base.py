# tools/base.py
from abc import ABC, abstractmethod
from typing import Any, Dict, List

class BaseTool(ABC):
    name: str

    @abstractmethod
    def run(self, query: str, **kwargs) -> List[Dict[str, Any]]:
        """
        Execute a tool action (e.g., web search) and return structured results.
        """
        pass