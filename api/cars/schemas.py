from datetime import date
from unittest.mock import Base
from pydantic import BaseModel, ConfigDict, Field
from sqlalchemy import desc

from exts.enums import FuelType, TransmissionType


class CarBase(BaseModel):
    car_brand: str
    car_model: str
    release_date: date = Field(..., description="You have to put date in 'YYYY-MM-DD' format.")
    fuel_type: FuelType
    transmission_type: TransmissionType
    mileage: int = Field(
        ...,
        description="You have to put your car's mileage in kilometers"
    )
    price: int = Field(
        ...,
        description="You have to put your car's price in Rubles"
    )


class CarCreate(CarBase):
    pass


class CarUpdate(CarBase):
    pass


class CarUpdatePartitital(CarBase):
    car_brand: str | None
    car_model: str | None
    release_date: date | None
    fuel_type: FuelType | None
    transmission_type: TransmissionType | None
    mileage: int | None
    price: int | None


class Car(CarBase):
    model_config = ConfigDict(from_attributes=True)

    id: int