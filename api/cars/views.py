from fastapi import APIRouter, Body, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models.users import User
from core.models import db_helper

from ..dependencies import get_current_user

from . import crud
from .dependencies import car_by_id, get_pagination_params
from .schemas import Car, CarCreate, CarFilter


router = APIRouter(tags=["Cars"])

@router.get("/{car_id}", response_model=Car)
async def get_car(
    car: Car = Depends(car_by_id),
    user: User = Depends(get_current_user)
):
    return car


@router.get("/")
async def get_car_by_filters(
    car_filter: CarFilter = Depends(),
    pagination: dict = Depends(get_pagination_params),
    user: User = Depends(get_current_user),
    session: AsyncSession = Depends(db_helper.session_dependency)
):
    limit = pagination["limit"]
    offset = pagination["offset"]
    return await crud.get_car_by_filters(session, car_filter, limit, offset)


@router.post("/", response_model=CarCreate)
async def create_car(
    car_in: CarCreate,
    user: User = Depends(get_current_user),
    session: AsyncSession = Depends(db_helper.session_dependency)
):
    car: Car = await crud.create_car(session, car_in)
    return car