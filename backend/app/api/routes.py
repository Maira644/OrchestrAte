from fastapi import APIRouter
from app.core.config import settings

router = APIRouter()


@router.get("/")
def root():
    return {
        "message": "Welcome to OrchestrAte API",
        "algorithm": settings.ALGORITHM
    }


@router.get("/health")
def health_check():
    return {
        "status": "healthy"
    }