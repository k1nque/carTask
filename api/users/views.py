from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from api.users.auth import get_password_hash
from core.models import db_helper
from .schemas import UserRegister
from . import crud

router = APIRouter(tags=['auth'])

@router.post("/register")
async def register_user(
    user_in: UserRegister,
    session: AsyncSession = Depends(db_helper.session_dependency)
):
    usr = await crud.find_user(session, user_in.username)
    if usr:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with such username already exists"
        )
    psw_hash = get_password_hash(user_in.password)
