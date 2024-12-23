from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from app.schemas import user
from app.services.user_service import UserService
from app.core.database import get_db
from app.core.utils import hash_password

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/create-user", response_model=user.UserOut, status_code=status.HTTP_201_CREATED)
async def create_user(new_user: user.UserCreate, db: Session = Depends(get_db)):
    user_service = UserService(db=db)

    # Hash the password before saving
    new_user.hashed_password = hash_password(new_user.hashed_password)

    try:
        created_user = await user_service.create_user(new_user)
        return created_user
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
