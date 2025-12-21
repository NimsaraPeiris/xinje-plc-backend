from fastapi import APIRouter, HTTPException

from app.services.chains.base_chain import chat_chain_simple

router = APIRouter()

@router.post("/")
async def get_ai_response(request):
    try:
        result = chat_chain_simple(request)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))