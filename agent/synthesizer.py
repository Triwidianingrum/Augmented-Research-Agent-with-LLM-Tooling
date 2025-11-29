# agent/synthesizer.py

from typing import List, Dict, Any

class Synthesizer:

    def __init__(self, llm):
        self.llm = llm

    def synthesize(self, research_chunks: List[Dict[str, Any]]) -> Dict[str, Any]:

        sections = []
        contradictions_and_uncertainities = []
        citations = []

        # -------------------- Build Sections ------------------------
        for idx, chunk in enumerate(research_chunks, start=1):

            task = chunk.get("task")

            if chunk.get("summary"):
                summary = chunk["summary"]
            else:
                # Build raw text for Gemini summarization
                text = ""
                for r in chunk.get("results", []):
                    text += f"- {r.get('snippet','')}\n"

                if text.strip():
                    prompt = (
                        f"Summarize the following research findings for the task:\n"
                        f"Task: {task}\n\n"
                        f"{text}\n"
                    )
                    summary = self.llm.complete(prompt)
                else:
                    summary = f"{task}: No data available."

            sections.append({
                "order": idx,
                "content": summary
            })

        # -------------------- Build Citations ------------------------
        url_map = {}
        cid = 1

        for chunk in research_chunks:
            for r in chunk.get("results", []):
                url = r.get("url")
                if url and url not in url_map:
                    url_map[url] = cid
                    cid += 1

        for url, cid in url_map.items():
            citations.append({"id": cid, "url": url})

        # -------------------- Build Conclusion ------------------------
        if sections:
            last = sections[-1]["content"]
            conclusion = self.llm.complete(f"Give a concluding statement:\n{last}")
        else:
            conclusion = "No conclusion available."

        return {
            "sections": sections,
            "conclusion": conclusion,
            "contradictions_and_uncertainities": [],
            "citations": citations
        }
