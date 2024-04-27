from passlib.context import CryptContext
from fastapi import APIRouter

import db
from enitites import UserEntity
from models import User

router = APIRouter()

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.get("/users", tags=["users"])
async def get_all_users(id: int = None):
    if id is None:
        return db.db.query(UserEntity).all()
    else:
        return db.db.get(UserEntity, id)


@router.post("/users/create", tags=["users"])
async def create_user(user: User):
    hashed_password = password_context.hash(user.password)
    new_user = UserEntity(first_name=user.first_name, last_name=user.last_name, email=user.email, password=hashed_password)
    db.db.add(new_user)
    db.db.commit()
    return {"user": user}