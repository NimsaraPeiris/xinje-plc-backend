from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

def get_llm(model_name: str = "gemini-3-flash-preview"):
    """
    Factory function to initialize the LLM with consistent settings.
    """
    return ChatGoogleGenerativeAI(
        model=model_name,
    )

def get_vision_llm(model_name: str = "meta-llama/llama-4-scout-17b-16e-instruct"):
    """
    Vision model specifically for analyzing PLC diagrams or sketches.
    """
    return ChatGroq(
        model=model_name,
    )