from pydantic import BaseModel, Field


class UserBase(BaseModel):
    username: str
    password: str = Field(min_length=6, max_length=30, description="Password. Min: 6 chars, Max: 30 chars")


class UserRegister(UserBase):
    pass


class UserLogin(UserBase):
    pass