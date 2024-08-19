from sqlalchemy.ext.asyncio import AsyncSession

from exts.enums import FuelType, TransmissionType

from .schemas import CarCreate
from core.models import Car


async def create_car(session: AsyncSession, car_in: CarCreate):
    car_params = car_in.model_dump()
    print(car_params)
    car_params["fuel_type"] = car_params["fuel_type"].value
    car_params["transmission_type"] = car_params["transmission_type"].value
    car = Car(**car_params)
    session.add(car)
    await session.commit()
    await session.refresh(car)
    return car


async def get_car(session: AsyncSession, car_id: int) -> Car | None:
    return await session.get(Car, car_id)
