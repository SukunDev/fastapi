from .service import Service
from sqlalchemy.orm import Session
from app.models.user import User


class UserService(Service):
    def __init__(self):
        super().__init__()

    def get_users(self, db: Session):
        users = db.query(User).all()
        return self.response(
            code=200,
            message="Success retrieving users",
            data=[{"id": u.id, "name": u.name, "email": u.email} for u in users]
        )

    def get_user_by_id(self, db: Session, user_id: int):
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            return self.response(
                code=404,
                message="User not found",
                error="User not found"
            )
        return self.response(
            code=200,
            message="Success retrieving user",
            data={
                "id": user.id,
                "name": user.name,
                "email": user.email
            }
        )

    def update_user(self, db: Session, user_id: int, name: str = None, email: str = None):
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            return self.response(
                code=404,
                message="User not found",
                error="User not found"
            )

        if name:
            user.name = name
        if email:
            user.email = email

        db.commit()
        db.refresh(user)

        return self.response(
            code=200,
            message="User updated successfully",
            data={
                "id": user.id,
                "name": user.name,
                "email": user.email
            }
        )

    def delete_user(self, db: Session, user_id: int):
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            return self.response(
                code=404,
                message="User not found",
                error="User not found"
            )

        db.delete(user)
        db.commit()

        return self.response(
            code=200,
            message="User deleted successfully",
            data={"id": user_id}
        )
