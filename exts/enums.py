from enum import Enum

class FuelType(str, Enum):
    petrol = "petrol"
    diesel = "diesel"
    electricity = "electricity"
    hybrid = "hybrid"


class TransmissionType(str, Enum):
    manual = "manual"
    automatic = "automatic"
    cvt = "cvt"
    robot = "robot"