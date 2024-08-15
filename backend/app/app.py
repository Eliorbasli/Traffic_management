from fastapi import FastAPI
from app.core.config import settings
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from contextlib import asynccontextmanager

from app.models.user_model import User
from app.api.api_v1.router import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
        initialize crucial application services
    """
    db_client = AsyncIOMotorClient(settings.MONGO_CONNECTION_STRING).trafficmanagement
    await init_beanie(
        database=db_client,
        document_models= [
            User
        ]
    )
    
    #the start up part
    yield
    
    #The shutdown Part
    #(Place any cleanup code here if nedded)


app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    lifespan=lifespan
)

app.include_router(router , prefix=settings.API_V1_STR)