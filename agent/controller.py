# agent/controller.py
from typing import Dict, List, Any
from .task_decomposition import TaskDecomposer
from .synthesizer import Synthesizer

# __define-ocg__ – main orchestration entrypoint for the Deep Research Agent

class DeepResearchAgent:
    def __init__(self, llm, search_tool):
        self.llm = llm
        self.search = search_tool
        self.decomposer = TaskDecomposer(self.llm)
        self.synthesizer = Synthesizer(self.llm)   # VERY IMPORTANT: pass LLM

    def run(self, query: str) -> Dict[str, Any]:

        varOcg = {"query": query}  # required variable

        tasks = self.decomposer.decompose(query)

        research_chunks = []

        for task in tasks:
            results = self.search.run(query=task, n_results=5)

            research_chunks.append({
                "task": task,
                "results": results,
                "summary": None,
                "contradictions": [],
                "uncertainties": [],
                "citations": []
            })

        output = self.synthesizer.synthesize(research_chunks)
        return output
