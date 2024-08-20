from sqlalchemy import Result, Select
from sqlalchemy.ext.asyncio import AsyncSession

from core.models.users import User


async def find_user(session: AsyncSession, username: str) -> User | None:
    stmnt = Select(User).where(User.username == username)
    result: Result = await session.execute(stmnt)
    usr = result.scalar_one_or_none()
    return usr


async def create_user(session: AsyncSession, username: str, passw_hash: str) -> User:
    usr = User(
        username=username,
        password=passw_hash
    )
    session.add(usr)
    await session.commit()
    await session.refresh(usr)
    return usr