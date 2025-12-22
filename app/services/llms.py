from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

def get_llm(model_name: str = "gemini-3-flash-preview"):
    """
    Factory function to initialize the LLM with consistent settings.
    """
    return ChatGoogleGenerativeAI(
        model=model_name,
    )