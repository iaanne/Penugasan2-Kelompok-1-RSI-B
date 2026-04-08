from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.account import AccountCreate, AccountUpdate, AccountResponse
from app.services import account_service

router = APIRouter(prefix="/accounts", tags=["Accounts"])

@router.get("/", response_model=list[AccountResponse], summary="Get all accounts")
def get_accounts(db: Session = Depends(get_db)):
    return account_service.get_accounts(db)

@router.get("/{account_id}", response_model=AccountResponse, summary="Get accounts by ID")
def get_account(account_id: int, db: Session = Depends(get_db)):
    try:
        return account_service.get_account(db, account_id)
    except Exception:
        raise HTTPException(status_code=404, detail="Account not found")

@router.post("/", response_model=AccountResponse, summary="Create new account")
def create_account(data: AccountCreate, db: Session = Depends(get_db)):
    try:
        return account_service.create_account(db, data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{account_id}", response_model=AccountResponse, summary="Update account")
def update_account(account_id: int, data: AccountUpdate, db: Session = Depends(get_db)):
    try:
        return account_service.update_account(db, account_id, data)
    except Exception:
        raise HTTPException(status_code=404, detail="Account not found")

@router.delete("/{account_id}", summary="Delete role")
def delete_account(account_id: int, db: Session = Depends(get_db)):
    try:
        account_service.delete_account(db, account_id)
        return {"message": "Account deleted"}
    except Exception:
        raise HTTPException(status_code=404, detail="Account not found")
    
@router.patch("/{account_id}", response_model=AccountResponse, summary="Partially update account")
def patch_account(account_id: int, data: AccountUpdate, db: Session = Depends(get_db)):
    try:
        return account_service.update_account(db, account_id, data)
    except Exception:
        raise HTTPException(status_code=404, detail="Account not found")