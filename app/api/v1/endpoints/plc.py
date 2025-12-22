from fastapi import APIRouter
from app.services.chains.plc_generator import create_plc_chain
from pydantic import BaseModel, Field
from typing import Optional

router = APIRouter()
plc_chain = create_plc_chain()

class ChatResponse(BaseModel):
    response: str
    format: str

class TextRequest(BaseModel):
    message: str = Field(..., min_length=1, description="User's PLC programming requirement")
    output_format: Optional[str] = Field("LD", description="Output format: LD or IL")


@router.post("/chat/text", response_model=ChatResponse)
async def chat_text(request: TextRequest):

    response = await plc_chain.ainvoke({
        "input": request.message,
        "output_format": request.output_format
    })
    answer_text = response.get("answer")

    return ChatResponse(
        response=answer_text,
        format=request.output_format
    )