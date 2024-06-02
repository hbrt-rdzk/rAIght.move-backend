from fastapi import APIRouter

from app.api.api_v1.endpoints import explain

api_router = APIRouter()
api_router.include_router(explain.router, prefix="/explain", tags=["explain"])
