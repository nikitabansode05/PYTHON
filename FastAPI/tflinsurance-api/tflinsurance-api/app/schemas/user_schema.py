from pydantic import BaseModel, Field
from datetime import datetime

class UserCreate(BaseModel):
    username: str = Field(min_length=2, max_length=100)
    email: str = Field(min_length=2, max_length=100)
    password_hash: str
    status: str
   

class UserUpdate(BaseModel):
    username: str | None = None
    email: str | None = None
    password_hash: str | None = None
    status: str | None = None


class UserResponse(BaseModel):
    user_id: int
    username: str
    email: str
    password_hash: str
    status: str
    created_at: datetime
    updated_at: datetime | None = None

     