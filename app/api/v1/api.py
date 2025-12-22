from fastapi import APIRouter
from app.api.v1.endpoints import plc

api_router = APIRouter()
api_router.include_router(plc.router, prefix="/plc", tags=["Plc Code"])