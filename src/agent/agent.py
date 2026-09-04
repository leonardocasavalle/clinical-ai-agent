from typing import Dict
from src.llm.llm import LLMClient
from src.agent.rag import SimpleRAG


class ClinicalAIAgent:
    """
    Core orchestration layer for the Clinical AI Agent.
    """

    def __init__(self, name: str = "Clinical AI Agent"):
        self.name = name
        self.llm = LLMClient()
        self.rag = SimpleRAG()

    def process_query(self, query: str) -> Dict[str, str]:
        """
        Process a user query using the LLM and RAG.
        """

        documents = self.rag.retrieve(query)

        context = "\n\n".join(
            document["content"] for document in documents
        )

        response = self.llm.generate(
            f"Responde la pregunta usando el siguiente contexto:\n\n"
            f"{context}\n\n"
            f"Pregunta: {query}"
        )

        return {
            "agent": self.name,
            "query": query,
            "status": "completed",
            "response": response
        }