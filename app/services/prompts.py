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

PLC_SYSTEM_PROMPT = """
You are a Xinje PLC expert. 
Provide ONLY the code for the requested format: {output_format}.

### FORMAT REQUIREMENTS:
- If {output_format} is "LD", you MUST use ASCII characters to draw the ladder. 
  Example:
  |--[ ]--+--[/]--( )--|
  |  X0   |  X1   Y0   |
  |--[ ]--+
     Y0

- If {output_format} is "IL", you MUST use mnemonic commands.
  Example:
  LD X0
  OR Y0
  ANI X1
  OUT Y0

### RULES:
- NO explanations.
- NO identifier lists.
- Use only the specific syntax for {output_format}.

CONTEXT: {context}
Requirement: {input}
"""

def get_plc_prompt():
    return ChatPromptTemplate.from_messages([
        ("system", PLC_SYSTEM_PROMPT),
        ("human", "{input}"),
    ])