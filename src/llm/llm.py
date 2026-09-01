class LLMClient:
    """
    Interface for interacting with a Large Language Model.
    """

    def __init__(self, model_name="default"):
        self.model_name = model_name

    def generate(self, prompt):
        """
        Generate a response from the LLM.
        """
        return f"LLM response to: {prompt}"
