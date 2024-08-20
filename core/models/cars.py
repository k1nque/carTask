from datetime import date
from sqlalchemy.orm import Mapped

from exts.enums import TransmissionType, FuelType

from .base import Base

class Car(Base):
    __tablename__ = "cars"
    brand: Mapped[str]
    model: Mapped[str]
    release_date: Mapped[date]
    fuel_type: Mapped[FuelType]
    transmission: Mapped[TransmissionType]
    mileage: Mapped[int]
    price: Mapped[int]
