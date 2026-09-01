import os
from google import genai


class LLMClient:
    """
    Interface for interacting with a Large Language Model.
    """

    def __init__(self, model_name="gemini-3.6-flash"):
        self.model_name = model_name

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY environment variable is not set."
            )

        self.client = genai.Client(api_key=api_key)

    def generate(self, prompt):
        """
        Generate a response from Gemini.
        """

        response = self.client.models.generate_content(
            model=self.model_name,
            contents=prompt
        )

        return response.text
