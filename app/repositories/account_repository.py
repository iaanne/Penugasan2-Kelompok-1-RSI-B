from sqlalchemy.orm import Session
from app.models.role import Role

def get_all(db: Session):
    return db.query(Role).all()

def get_by_id(db: Session, role_id: int):
    return db.query(Role).filter(Role.id == role_id).first()

def create(db: Session, data):
    role = Role(**data.dict())
    db.add(role)
    db.commit()
    db.refresh(role)
    return role

def update(db: Session, role, data):
    for key, value in data.dict(exclude_unset=True).items():
        setattr(role, key, value)
    db.commit()
    db.refresh(role)
    return role

def delete(db: Session, role):
    db.delete(role)
    db.commit()