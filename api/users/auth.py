from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta, timezone

import os

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET = os.environ.get("SECRET_KEY")
ALGO = os.environ.get("ALGORITHM")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(days=30)
    to_encode.update({"exp": expire})
    encode_jwt = jwt.encode(to_encode, SECRET, algorithm=ALGO)
    return encode_jwt