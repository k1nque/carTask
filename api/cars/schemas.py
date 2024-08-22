from datetime import date
from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator

from exts.enums import FuelType, TransmissionType



class CarFilter(BaseModel):
    brand: str | None = None
    model: str | None = None
    fuel_type: FuelType | None = None
    transmission: TransmissionType | None = None
    mileage_min: int = 0
    mileage_max: int = 1_000_000
    price_min: int = 0
    price_max: int = 1_000_000_000

    @model_validator(mode="after")
    def validator(self):
        if self.mileage_min is not None and self.mileage_max is not None:
            assert (
                self.mileage_min < self.mileage_max
            ), "Mileage_min value must be less than mileage_max value"

            assert (
                self.mileage_min > 0 or self.mileage_max > 0
            ), "Mileage_min and mileage_max values cannot be negative number"
        elif self.mileage_min is None and self.mileage_max is not None:
            assert (
                self.mileage_max > 0
            ), "Mileage_max value cannot be negative number"
        elif self.mileage_min is not None and self.mileage_max is None:
            assert (
                self.mileage_min > 0
            ), "Mileage_min value cannot be negative number"

        if self.price_min is not None and self.price_max is not None:
            assert (
                self.price_min < self.price_max
            ), "Price_min value must be less than price_max value"

            assert (
                self.price_min > 0 or self.price_max > 0
            ), "Price_min and price_max values cannot be negative number"
        elif self.price_min is not None and self.price_max is None:
            assert (
                self.price_min > 0
            ), "Price_min value cannot be negative number"
        elif self.price_min is None and self.price_max is not None:
            assert (
                self.price_max > 0
            ), "Price_max value cannot be negative number"
        return self
            

class CarBase(BaseModel):
    brand: str
    model: str
    release_date: date | int = Field(..., description="You have to put date in 'YYYY-MM-DD' format or just a year in 'YYYY' format.")
    fuel_type: FuelType
    transmission: TransmissionType
    mileage: int = Field(
        ...,
        description="You have to put your car's mileage in kilometers"
    )
    price: int = Field(
        ...,
        description="You have to put your car's price in Rubles"
    )

    @field_validator("release_date")
    @classmethod
    def date_validator(cls, v: date | int):
        if isinstance(v, int):
            assert (
                1910 < v <= date.today().year
            ), f"Year must be in period: 1911-{date.today().year()}"
            return date(year=v, month=1, day=1)
        else:
            return v


class CarCreate(CarBase):
    pass


    @model_validator(mode="after")
    def validator(self):
        assert (
            len(self.brand) < 25
        ), "Brand length cannot be much than 25 chars"
        assert (
            len(self.model) < 40
        ), "Model length cannot be much than 40 chars"
        assert (
            0 <= self.mileage <= 1_000_000
        ), "Mileage cannot be less than 0 km and much than 1 000 000 km"
        assert (
            0 <= self.price <= 1_000_000_000
        ), "Price cannot be less than 0 rub and much than 1 000 000 000 rub"
        return self
    

class CarUpdate(CarBase):
    pass


class CarUpdatePartitital(CarBase):
    brand: str | None = None
    model: str | None = None
    release_date: date | int | None = None
    fuel_type: FuelType | None = None
    transmission: TransmissionType | None = None
    mileage: int | None = None
    price: int | None = None


class Car(CarBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
