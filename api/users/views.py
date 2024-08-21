from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.ext.asyncio import AsyncSession

from api.users.auth import (
    create_access_token,
    authenticate_user,
    get_password_hash,
)
from core.models import db_helper
from .schemas import UserLogin, UserRegister
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
    usr = await crud.create_user(session, user_in.username, psw_hash)
    return {"message": "You are registered succefully"}


@router.post("/login")
async def auth_user(
    response: Response,
    user_in: UserLogin,
    session: AsyncSession = Depends(db_helper.session_dependency)
):
    check = await authenticate_user(session, username=user_in.username, password=user_in.password)
    if check is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Wrong username or password (or both xD)')
    access_token = create_access_token({"sub": str(check.id)})
    response.set_cookie(key="users_access_token", value=access_token, httponly=True)
    return {'access_token': access_token, 'refresh_token': None}


@router.post("/logout")
async def logout_user(
    response: Response
):
    response.delete_cookie(key="users_access_token")
    return {"message": "Logged out"}