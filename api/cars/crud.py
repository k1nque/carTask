from sqlalchemy import Result, Select
from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import CarCreate, CarFilter
from core.models import Car


async def get_car_by_filters(
    session: AsyncSession,
    car_filter: CarFilter,
    limit: int,
    offset: int
):
    stmnt = Select(Car).where(
        (Car.brand == car_filter.brand if car_filter.brand else True) and
        (Car.model == car_filter.model if car_filter.model else True) and
        (
            Car.fuel_type == car_filter.fuel_type
            if car_filter.fuel_type is not None else True
        ) and
        (
            Car.transmission == car_filter.transmission
            if car_filter.transmission else True
        ) and
        (Car.mileage.between(car_filter.mileage_min, car_filter.mileage_max)) and
        (Car.price.between(car_filter.price_min, car_filter.price_max))
    ).offset(offset).limit(limit)

    result: Result = await session.execute(stmnt)
    cars = result.scalars().all()
    return list(cars)


async def create_car(session: AsyncSession, car_in: CarCreate):
    car_params = car_in.model_dump()
    print(car_params)
    car_params["fuel_type"] = car_params["fuel_type"].value
    car_params["transmission"] = car_params["transmission"].value
    car = Car(**car_params)
    session.add(car)
    await session.commit()
    await session.refresh(car)
    return car


async def get_car(session: AsyncSession, car_id: int) -> Car | None:
    return await session.get(Car, car_id)
