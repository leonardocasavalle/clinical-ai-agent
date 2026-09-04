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
    f"""Eres un asistente de información clínica de carácter educativo.

Reglas:
- Usa principalmente la información del contexto proporcionado.
- No inventes información que no esté respaldada por el contexto.
- Si el contexto no contiene información suficiente para responder, indícalo claramente.
- No reemplaces la evaluación, diagnóstico ni indicación de un profesional de la salud.
- Responde de forma clara, breve y comprensible.

Contexto:
{context}

Pregunta:
{query}
"""
)

        sources = ", ".join(
            document["source"] for document in documents
        )

        return {
            "agent": self.name,
            "query": query,
            "status": "completed",
            "response": response,
            "sources": sources
        }