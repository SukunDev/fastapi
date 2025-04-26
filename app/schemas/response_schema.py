from typing import Generic, TypeVar, Optional
from pydantic import BaseModel, ConfigDict

T = TypeVar('T')

class ResponseSchema(BaseModel, Generic[T]):
    model_config = ConfigDict(from_attributes=True)

    status: bool
    data: T
    message: str
    error: Optional[str] = None
