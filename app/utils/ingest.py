from app.services.vector_store import get_vector_store
from app.utils.document_processor import load_plc_data 

def ingest_plc_knowledge(json_file_path: str):

    print(f"Loading data from {json_file_path}...")
    docs = load_plc_data(json_file_path)
    
    vector_db = get_vector_store()
    
    print(f"Adding {len(docs)} mnemonics to the vector store...")
    vector_db.add_documents(docs)
    
    print("✅ Ingestion complete. Vector store is ready!")

if __name__ == "__main__":
    # python -m app.utils.ingest
    ingest_plc_knowledge("data/plc_dictionary.json")