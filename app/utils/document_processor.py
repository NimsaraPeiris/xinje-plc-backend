import json
import os
from langchain_core.documents import Document

def load_plc_data(file_path: str):
    """
    Reads a JSON file of mnemonics and converts them into LangChain Documents.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Mnemonic file not found at: {file_path}")

    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    docs = []
    for item in data:
        content = f"Function: {item.get('function', '')}. Description: {item.get('description', '')}"
        metadata = {
            "mnemonic": item.get("mnemonic", "UNKNOWN"),
            "category": item.get("category", "General"),
            "source": file_path
        }
        
        docs.append(Document(page_content=content, metadata=metadata))
    
    return docs