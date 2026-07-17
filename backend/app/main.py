from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="OrchestrAte API",
    description="Multi-Agent Restaurant Management System",
    version="1.0.0"
)

app.include_router(router)