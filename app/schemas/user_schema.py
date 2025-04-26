from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

class UserResponse(BaseModel):
    id: int = 1
    name: str
    email: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)



class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None