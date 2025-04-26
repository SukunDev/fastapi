from .service import Service
from app.utils.helper import verify_password, hash_password
from app.utils.jwt_handler import create_access_token
from sqlalchemy.orm import Session
from app.models import User


class AuthService(Service):
    def __init__(self):
        super().__init__()

    def register(self, db: Session, name: str, email: str, password: str):
        existing_user = db.query(User).filter(User.email == email).first()
        if existing_user:
            return self.response(
                code=400,
                message="User already exists",
                error="Email is already registered"
            )
        hashed_password = hash_password(password)
        new_user = User(name=name, email=email, password=hashed_password)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return self.response(
            code=201,
            message="User registered successfully",
            data={
                "name": new_user.name,
                "email": new_user.email
            }
        )

    def login(self, db: Session, email: str, password: str):
        user = db.query(User).filter(User.email == email).first()
        if not user or not verify_password(password, user.password):
            return self.response(
                code=401,
                message="Failed to login",
                error="Invalid credentials"
            )

        return self.response(
            code=200,
            message="Success to login",
            data={
                "access_token": create_access_token({"sub": user.email})
            }
        )
