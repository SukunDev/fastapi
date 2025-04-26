from typing import List
from fastapi import APIRouter, Depends
from app.utils.deps import get_current_user
from sqlalchemy.orm import Session
from app.database import get_db
from app.services import UserService
from app.schemas import ResponseSchema, UserResponse, UserUpdate

router = APIRouter()
userServices = UserService()


@router.get("/", response_model=ResponseSchema[List[UserResponse]])
def get_users(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    return userServices.get_users(db=db)

@router.get("/{user_id}", response_model=ResponseSchema[UserResponse])
def get_user(user_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    return userServices.get_user_by_id(db=db, user_id=user_id)

@router.put("/{user_id}", response_model=ResponseSchema[UserResponse])
def update_user(user_id: int, payload: UserUpdate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    return userServices.update_user(db=db, user_id=user_id, name=payload.name, email=payload.email)

@router.delete("/{user_id}", response_model=ResponseSchema[dict])
def delete_user(user_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    return userServices.delete_user(db=db, user_id=user_id)
