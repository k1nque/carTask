from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta, timezone
from sqlalchemy.ext.asyncio import AsyncSession

from settings import get_auth_data
from . import crud

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(days=30)
    to_encode.update({"exp": expire})
    auth_data = get_auth_data()
    encode_jwt = jwt.encode(
        to_encode,
        auth_data["secret_key"],
        algorithm=auth_data["algorithm"])
    return encode_jwt


async def authenticate_user(session: AsyncSession, username: str, password: str):
    user = await crud.find_user_by_username(session, username)
    if user and verify_password(plain_password=password, hashed_password=user.password):
        return user
    return None