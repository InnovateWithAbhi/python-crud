from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, Field

class UserBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    first_name: str = Field(..., min_length=1, max_length=50)
    last_name: str = Field(..., min_length=1, max_length=50)
    phone_number: str = Field(..., min_length=10, max_length=15)
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False

class UserCreate(UserBase):
    hashed_password: str

class UserInDB(UserBase):
    id: int
    hashed_password: str
    created_on: datetime
    updated_on: datetime

    class Config:
        orm_mode = True

class UserUpdate(UserBase):
    hashed_password: Optional[str] = None

class UserOut(UserBase):
    id: int

    class Config:
        orm_mode = True