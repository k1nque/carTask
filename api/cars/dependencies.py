from enum import Enum
from typing import Annotated

from fastapi import Path, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper

from . import crud



async def car_by_id(
    car_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    car = await crud.get_car(session, car_id)
    if car is not None:
        return car
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Car {car_id} is not found!"
    )


def get_pagination_params(
    offset: int = Query(0, ge=0),
    limit: int = Query(10, gt=0)
):
    return {"offset": offset, "limit": limit}
