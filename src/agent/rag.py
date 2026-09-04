from pathlib import Path


class SimpleRAG:
    """
    Simple document retrieval layer for the Clinical AI Agent.
    """

    def __init__(self, documents_path="src/data/docs"):
        self.documents_path = Path(documents_path)

    def load_documents(self):
        """
        Load all Markdown documents from the documents directory.
        """
        documents = []

        for file in self.documents_path.glob("*.md"):
            documents.append({
                "source": str(file),
                "content": file.read_text(encoding="utf-8")
            })

        return documents

    def retrieve(self, query):
        """
        Retrieve documents containing relevant words from the query.
        """
        documents = self.load_documents()

        query_words = set(query.lower().split())

        results = []

        for document in documents:
            content_lower = document["content"].lower()

            if any(word in content_lower for word in query_words):
                results.append(document)

        return results
