# agent/task_decomposition.py

from __future__ import annotations
from typing import List
from models.base import LLMBase

class TaskDecomposer:
    """
    Turns a single research query into a small list of sub-tasks.
    __define-ocg__ – this decomposer feeds the overall research pipeline.
    """

    def __init__(self, llm: LLMBase) -> None:
        self.llm = llm

    def decompose(self, query: str) -> list[str]:
        """
        Use the LLM to break the query into 3–7 concrete research tasks.

        Returns:
            list[str]: clean task descriptions without numbering.
        """

        prompt = (
            "You are a research planning assistant.\n\n"
            "Break the following question into 3–7 meaningful research tasks.\n"
            "Return ONLY a numbered list (1., 2., 3.)\n\n"
            "Example:\n"
            "1. Identify key factors...\n"
            "2. Evaluate existing methods...\n"
            "3. Summarize industry applications...\n\n"
            "User query:\n"
            f"\"\"\"{query}\"\"\"\n"
        )

        raw = self.llm.complete(prompt)

        tasks: List[str] = []
        for line in raw.splitlines():
            line = line.strip()
            if not line:
                continue

            # Matches: 1. Task ... OR 1) Task ...
            if line[0].isdigit():
                i = 1
                while i < len(line) and (line[i].isdigit() or line[i] in ".)"):
                    i += 1
                task_text = line[i:].lstrip()
                if task_text:
                    tasks.append(task_text)

        if not tasks:
            tasks = [query]

        return tasks
