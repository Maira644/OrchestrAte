from fastapi import FastAPI

from app.api.routes import router
from app.api.menu import router as menu_router
from app.api.inventory import router as inventory_router

app = FastAPI(
    title="OrchestrAte API",
    description="Multi-Agent Restaurant Management System",
    version="1.0.0"
)

app.include_router(router)
app.include_router(menu_router)
app.include_router(inventory_router)