from fastapi import APIRouter
from app.controllers import auth_controller, user_controller

api_router = APIRouter()

api_router.include_router(auth_controller.router, prefix="/api", tags=["Auth"])
api_router.include_router(user_controller.router, prefix="/api/users", tags=["Users"])
