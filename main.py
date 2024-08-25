from fastapi import FastAPI
from app.api.routes import router
from app.core.config import settings

app = FastAPI(title=settings.app_name, version=settings.version)

app.include_router(router)