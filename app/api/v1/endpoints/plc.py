from fastapi import APIRouter
from fastapi import  File, UploadFile, Form, HTTPException
from app.services.chains.plc_generator import create_plc_chain
from pydantic import BaseModel, Field
import base64
from typing import Optional
from app.services.llms import get_vision_llm

router = APIRouter()
plc_chain = create_plc_chain()
vision_llm = get_vision_llm()

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


@router.post("/chat/image", response_model=ChatResponse)
async def chat_image(
    image: UploadFile = File(...),
    message: Optional[str] = Form(None),
    output_format: Optional[str] = Form("LD")
):

    if not image.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image")

    image_data = await image.read()
    base64_image = base64.b64encode(image_data).decode('utf-8')

    vision_prompt = "Describe the PLC logic shown in this image in technical detail."

    vision_description = await vision_llm.ainvoke([
        {
            "role": "user",
            "content": [
                {"type": "text", "text": vision_prompt},
                {
                    "type": "image_url", 
                    "image_url": {"url": f"data:{image.content_type};base64,{base64_image}"}
                }
            ]
        }
    ])

    combined_query = f"{message}\nImage Analysis: {vision_description.content}"
    
    response = await plc_chain.ainvoke({
        "input": combined_query,
        "output_format": output_format
    })

    return ChatResponse(
        response=response.get("answer"),
        format=output_format
    )