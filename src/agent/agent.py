from typing import Dict
from src.llm.llm import LLMClient


class ClinicalAIAgent:
    """
    Core orchestration layer for the Clinical AI Agent.
    """

    def __init__(self, name: str = "Clinical AI Agent"):
        self.name = name
        self.llm = LLMClient()

    def process_query(self, query: str) -> Dict[str, str]:
        """
        Process a user query using the LLM.
        """

        response = self.llm.generate(query)

        return {
            "agent": self.name,
            "query": query,
            "status": "completed",
            "response": response
        }
