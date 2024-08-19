from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from .dependencies import car_by_id
from core.models import db_helper

from .schemas import Car, CarCreate


router = APIRouter(tags=["Cars"])

@router.get("/{car_id}", response_model=Car)
async def get_car(
    car: Car = Depends(car_by_id)
):
    return car


@router.post("/", response_model=CarCreate)
async def create_car(
    car_in: CarCreate,
    session: AsyncSession = Depends(db_helper.session_dependency)
):
    car: Car = await crud.create_car(session, car_in)
    return car