from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.role import RoleCreate, RoleUpdate, RoleResponse
from app.services import role_service

router = APIRouter(prefix="/roles", tags=["Roles"])

@router.get("/", response_model=list[RoleResponse])
def get_roles(db: Session = Depends(get_db)):
    return role_service.get_roles(db)

@router.get("/{role_id}", response_model=RoleResponse)
def get_role(role_id: int, db: Session = Depends(get_db)):
    try:
        return role_service.get_role(db, role_id)
    except:
        raise HTTPException(status_code=404, detail="Role not found")

@router.post("/", response_model=RoleResponse)
def create_role(data: RoleCreate, db: Session = Depends(get_db)):
    return role_service.create_role(db, data)

@router.put("/{role_id}", response_model=RoleResponse)
def update_role(role_id: int, data: RoleUpdate, db: Session = Depends(get_db)):
    try:
        return role_service.update_role(db, role_id, data)
    except:
        raise HTTPException(status_code=404, detail="Role not found")

@router.delete("/{role_id}")
def delete_role(role_id: int, db: Session = Depends(get_db)):
    try:
        role_service.delete_role(db, role_id)
        return {"message": "Role deleted"}
    except:
        raise HTTPException(status_code=404, detail="Role not found")