from sqlalchemy import Result, Select
from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import CarCreate, CarFilter, CarUpdate
from core.models import Car


async def get_car_by_filters(
        session: AsyncSession,
        car_filter: CarFilter,
        limit: int,
        offset: int
):
    stmnt = Select(Car)
    if car_filter.brand:
        stmnt = stmnt.filter_by(brand=car_filter.brand)
    if car_filter.model:
        stmnt = stmnt.filter_by(model=car_filter.model)
    if car_filter.fuel_type:
        stmnt = stmnt.filter_by(fuel_type=car_filter.fuel_type)
    if car_filter.transmission:
        stmnt = stmnt.filter_by(transmission=car_filter.transmission)
    stmnt = stmnt.where(
        Car.mileage.between(
            car_filter.mileage_min,
            car_filter.mileage_max
        ),
        Car.price.between(
            car_filter.price_min,
            car_filter.price_max
        ),
        Car.release_date.between(
            car_filter.date_min,
            car_filter.date_max
        )
    ).order_by(Car.id).offset(offset).limit(limit)

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


async def update_car(
        session: AsyncSession,
        car: Car,
        car_update: CarUpdate,
        partial: bool = False
):
    for key, val in car_update.model_dump(exclude_unset=partial).items():
        if val:
            setattr(car, key, val)
    await session.commit()
    return car


async def delete_car(session: AsyncSession, car: Car) -> None:
    await session.delete(car)
    await session.commit()