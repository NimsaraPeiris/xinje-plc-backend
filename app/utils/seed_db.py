from app.utils.document_processor import load_plc_data
from app.services.vector_store import get_vector_store

def seed():
    print("Initializing seed process...")
    # 1. Load data from JSON
    docs = load_plc_data("data/plc.json")
    
    # 2. Get vector store instance
    vector_db = get_vector_store()
    
    # 3. Add to database
    print(f"Adding {len(docs)} mnemonics to vector store...")
    vector_db.add_documents(docs)
    print("Seed complete! Your vector store is now ready.")

if __name__ == "__main__":
    seed()