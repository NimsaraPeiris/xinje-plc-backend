import os
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

def get_embeddings():
    return  HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

def get_vector_store():
    """
    Connects to the persistent ChromaDB instance on disk.
    """
    embeddings = get_embeddings()

    if not os.path.exists("data/chroma_db"):
        os.makedirs("data/chroma_db")

    persist_directory = "data/chroma_db"
    
    return Chroma(
        persist_directory=persist_directory,
        embedding_function=embeddings,
        collection_name="plc_mnemonics"
    )