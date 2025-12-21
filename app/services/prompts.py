from langchain_core.prompts import ChatPromptTemplate

def get_assistant_prompt():
    """
    Standard prompt for a general assistant.
    """
    return ChatPromptTemplate.from_messages([
        ("system", "You are a helpful AI assistant specialized in Data Science."),
        ("human", "{user_input}")
    ])

def get_rag_prompt():
    """
    Prompt specifically for Retrieval-Augmented Generation.
    """
    return ChatPromptTemplate.from_messages([
        ("system", "Answer the user's question based ONLY on the following context:\n\n{context}"),
        ("human", "{input}")
    ])