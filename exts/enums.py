from enum import Enum

class FuelType(Enum):
    petrol = "petrol"
    diesel = "diesel"
    electricity = "electricity"
    hybrid = "hybrid"


class TransmissionType(Enum):
    manual = "manual"
    automatic = "automatic"
    cvt = "cvt"
    robot = "robot"