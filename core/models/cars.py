from datetime import date
from sqlalchemy.orm import Mapped
from sqlalchemy.dialects.postgresql import ENUM

from exts.enums import TransmissionType, FuelType

from .base import Base

class Car(Base):
    __tablename__ = "cars"
    car_brand: Mapped[str]
    car_model: Mapped[str]
    release_date: Mapped[date]
    fuel_type: Mapped[FuelType]
    transmission_type: Mapped[TransmissionType]
    mileage: Mapped[int]
    price: Mapped[int]
