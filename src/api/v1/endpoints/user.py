from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.schema.user import UserCreate
from src.schema.user import UserBase as User
from src.core.security import get_current_user
from src.crud import user as user_crud
from src.core.database import get_db

router = APIRouter()


@router.get("/me", response_model=User)
def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user


@router.post("/users/", response_model=UserCreate)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return user_crud.create_user_entry(db, user)


@router.get("/users/{user_id}", response_model=UserCreate)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = user_crud.get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
