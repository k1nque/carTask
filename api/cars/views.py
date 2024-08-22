from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models.users import User
from core.models import db_helper

from ..dependencies import get_current_user

from . import crud
from .dependencies import car_by_id, get_pagination_params
from .schemas import Car, CarCreate, CarFilter, CarUpdate, CarUpdatePartitital


router = APIRouter(tags=["cars"])

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


@router.post("/", response_model=Car)
async def create_car(
    car_in: CarCreate,
    user: User = Depends(get_current_user),
    session: AsyncSession = Depends(db_helper.session_dependency)
):
    car: Car = await crud.create_car(session, car_in)
    return car


@router.put("/{car_id}", response_model=Car)
async def update_car(
    car_update: CarUpdate,
    car: Car = Depends(car_by_id),
    user: User = Depends(get_current_user),
    session: AsyncSession = Depends(db_helper.session_dependency)
):
    return await crud.update_car(session, car, car_update)


@router.patch("/{car_id}", response_model=Car)
async def update_car_partial(
    car_update: CarUpdatePartitital,
    car: Car = Depends(car_by_id),
    user: User = Depends(get_current_user),
    session: AsyncSession = Depends(db_helper.session_dependency)
):
    return await crud.update_car(session, car, car_update, True)


@router.delete("/{car_id}")
async def delete_car(
    car: Car = Depends(car_by_id),
    user: User = Depends(get_current_user),
    session: AsyncSession = Depends(db_helper.session_dependency)
):
    await crud.delete_car(session, car)