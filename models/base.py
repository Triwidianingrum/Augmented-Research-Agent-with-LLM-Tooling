# models/base.py
from abc import ABC, abstractmethod

class LLMBase(ABC):
    """
    Minimal base interface for any LLM client used in the Deep Research Agent.
    Implementations: MockLLM, GeminiLLM, etc.
    """

    @abstractmethod
    def complete(self, prompt: str) -> str:
        """
        Given a single text prompt, return a completion string.
        """
        raise NotImplementedError

