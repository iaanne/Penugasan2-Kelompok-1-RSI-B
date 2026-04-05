from pydantic import BaseModel
from typing import Optional

class RoleCreate(BaseModel):
    name: str

class RoleUpdate(BaseModel):
    name: Optional[str] = None

class RoleResponse(BaseModel):
    id: int
    name: str

    model_config = {"from_attributes": True}
