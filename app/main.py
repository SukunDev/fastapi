from fastapi import FastAPI
from app.routes import api_router
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="My Backend API",
    description="API with standard response schema",
    version="1.0.0"
)

app.include_router(api_router)
