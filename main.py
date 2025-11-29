import sys
from agent.controller import DeepResearchAgent
from models.gemini import GeminiLLM     # FIXED: import from gemini
from tools.google_search import GoogleSearchTool


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py \"your research query\"")
        sys.exit(1)

    query = sys.argv[1]

    agent = DeepResearchAgent(
        llm=GeminiLLM(),
        search_tool=GoogleSearchTool()
    )

    output = agent.run(query)
    print(output)


if __name__ == "__main__":
    main()
