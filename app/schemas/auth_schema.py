from pydantic import BaseModel

class RegisterSchema(BaseModel):
    name: str
    email: str
    password: str

class LoginSchema(BaseModel):
    email: str
    password: str

class LoginResponseSchema(BaseModel):
    access_token: str = "Bearer <token>"
