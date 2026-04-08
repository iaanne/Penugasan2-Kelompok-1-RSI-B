from sqlalchemy.orm import Session
from app.repositories import role_repository

def get_roles(db: Session):
    return role_repository.get_all(db)

def get_role(db: Session, role_id: int):
    role = role_repository.get_by_id(db, role_id)
    if not role:
        raise Exception("Role not found")
    return role

def create_role(db: Session, data):
    return role_repository.create(db, data)

def update_role(db: Session, role_id: int, data):
    role = role_repository.get_by_id(db, role_id)
    if not role:
        raise Exception("Role not found")
    return role_repository.update(db, role, data)

def delete_role(db: Session, role_id: int):
    role = role_repository.get_by_id(db, role_id)
    if not role:
        raise Exception("Role not found")
    role_repository.delete(db, role)