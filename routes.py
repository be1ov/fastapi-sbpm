from fastapi import APIRouter

import db
from enitites import UserModel

router = APIRouter()


@router.get("/users", tags=["users"])
async def get_all_users():
    return db.db.get(UserModel)