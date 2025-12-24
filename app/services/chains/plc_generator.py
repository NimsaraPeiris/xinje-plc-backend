from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from app.services.llms import get_llm
from app.services.prompts import get_plc_prompt
from app.services.vector_store import get_vector_store
from operator import itemgetter



def create_plc_chain():
    llm = get_llm()
    prompt = get_plc_prompt()
    vector_store = get_vector_store()
    retriever = vector_store.as_retriever()

    map_setup = RunnableParallel({
        "context": itemgetter("input") | retriever,
        "input": itemgetter("input"),
        "output_format": itemgetter("output_format")
    })

    chain = (
        map_setup 
        | RunnableParallel({
            "answer": prompt | llm | StrOutputParser(),
            "docs": itemgetter("context")
        })
    )
    
    return chain
