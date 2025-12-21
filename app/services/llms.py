from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

def get_llm(model_name: str = "openai/gpt-oss-120b"):
    """
    Factory function to initialize the LLM with consistent settings.
    """
    return ChatGroq(
        model=model_name,
    )