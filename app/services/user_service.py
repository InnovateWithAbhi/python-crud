from typing import Type

from fastapi import Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate

class UserService:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    async def create_user(self, new_user: UserCreate) -> User:
        # Check if username or email already exists
        existing_user = await self.get_by_username_or_email(new_user.username, str(new_user.email))
        if existing_user:
            raise ValueError("Username or email already exists")

        created_user = User(
            username=new_user.username,
            email=str(new_user.email),  # Convert EmailStr to str
            first_name=new_user.first_name,
            last_name=new_user.last_name,
            phone_number=new_user.phone_number,
            hashed_password=new_user.hashed_password,
            is_active=new_user.is_active,
            is_superuser=new_user.is_superuser,
        )
        self.db.add(created_user)
        self.db.commit()
        self.db.refresh(created_user)
        return created_user

    async def get_by_username_or_email(self, username: str, email: str) -> Type[User] | None:
        query = self.db.query(User).filter(
            (User.username == username) | (User.email == email)  # Use `|` for OR in SQLAlchemy
        )
        return query.first()
