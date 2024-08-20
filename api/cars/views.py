from fastapi import APIRouter, Depends, Header, Query
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from .dependencies import car_by_id, get_pagination_params
from core.models import db_helper

from .schemas import Car, CarCreate, CarFilter


router = APIRouter(tags=["Cars"])

@router.get("/{car_id}", response_model=Car)
async def get_car(
    car: Car = Depends(car_by_id)
):
    return car


@router.get("/")
async def get_car_by_filters(
    car_filter: CarFilter = Depends(),
    pagination: dict = Depends(get_pagination_params),
    session: AsyncSession = Depends(db_helper.session_dependency)
):
    limit = pagination["limit"]
    offset = pagination["offset"]
    return await crud.get_car_by_filters(session, car_filter, limit, offset)


@router.post("/", response_model=CarCreate)
async def create_car(
    car_in: CarCreate,
    session: AsyncSession = Depends(db_helper.session_dependency)
):
    car: Car = await crud.create_car(session, car_in)
    return car