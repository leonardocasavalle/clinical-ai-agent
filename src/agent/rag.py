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
        Retrieve documents ranked by relevant word matches.
        """

        documents = self.load_documents()

        stop_words = {
            "que", "qué", "es", "la", "el", "los", "las",
            "de", "del", "un", "una", "unos", "unas",
            "y", "o", "en", "por", "para", "con",
            "cuáles", "cuales", "cómo", "como",
            "qué", "que"
        }

        query_words = {
            word.strip("¿?¡!.,;:()[]{}\"'")
            for word in query.lower().split()
            if word.strip("¿?¡!.,;:()[]{}\"'") not in stop_words
        }

        results = []

        for document in documents:
            content_lower = document["content"].lower()

            score = sum(
                1
                for word in query_words
                if word in content_lower
            )

            if score > 0:
                results.append((score, document))

        results.sort(key=lambda item: item[0], reverse=True)

        return [document for score, document in results]