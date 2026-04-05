from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class AccountCreate(BaseModel):
    user_id: int
    role_id: int
    email: str
    username: str
    password: str

class AccountUpdate(BaseModel):
    email: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None

class AccountResponse(BaseModel):
    id: int
    user_id: int
    role_id: int
    email: str
    username: str
    created_at: datetime

    model_config = {"from_attributes": True}
