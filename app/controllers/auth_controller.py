from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.services import AuthService
from app.schemas import RegisterSchema, LoginSchema, ResponseSchema, LoginResponseSchema


router = APIRouter()
authServices = AuthService()

@router.post("/register", response_model=ResponseSchema[RegisterSchema])
def register(user: RegisterSchema, db: Session = Depends(get_db)):
  return authServices.register(db=db,name=user.name, email=user.email, password=user.password)

@router.post("/login", response_model=ResponseSchema[LoginResponseSchema])
def login(user: LoginSchema, db: Session = Depends(get_db)):
  return authServices.login(db=db, email=user.email, password=user.password)