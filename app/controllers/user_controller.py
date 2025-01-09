from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from pydantic import BaseModel

from app.db.database import get_db
from app.repositories.user_repository import UserRepository
from app.usecases.user_usecase import UserUseCase

router = APIRouter()
user_repo = UserRepository()
user_usecase = UserUseCase(user_repo)

# Request and Response Schemas
class UserCreateRequest(BaseModel):
    firstName: str
    lastName: str
    email: str
    mobileNumber: str
    password: str

class UserResponse(BaseModel):
    id: int
    userId: str
    firstName: str
    lastName: str
    email: str
    mobileNumber: str
    createdOn: str
    updatedOn: str
    isActive: bool

    class Config:
        from_attributes = True

@router.get("/", response_model=List[UserResponse])
def get_users(db: Session = Depends(get_db)):
    """Retrieve all users."""
    users = user_usecase.get_all_users(db)
    return users

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    """Retrieve a user by ID."""
    user = user_usecase.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    return user

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreateRequest, db: Session = Depends(get_db)):
    """Create a new user."""
    created_user = user_usecase.create_user(db, user.dict())
    return created_user

@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: UserCreateRequest, db: Session = Depends(get_db)):
    """Update an existing user."""
    updated_user = user_usecase.update_user(db, user_id, user.dict())
    if not updated_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    return updated_user

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    """Delete a user."""
    deleted_user = user_usecase.delete_user(db, user_id)
    if not deleted_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    return None
