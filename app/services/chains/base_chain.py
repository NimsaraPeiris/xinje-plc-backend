from app.services.llms import get_llm
from app.services.prompts import get_assistant_prompt
from langchain_core.output_parsers import StrOutputParser

def chat_chain_simple(user_input: str):
    llm = get_llm()
    prompt = get_assistant_prompt()
    output_parser = StrOutputParser()

    chain = prompt | llm | output_parser
    
    return chain.invoke({"user_input": user_input})