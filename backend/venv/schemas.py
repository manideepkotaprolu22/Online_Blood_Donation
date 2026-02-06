from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


class DonorCreate(BaseModel):
    name: str
    age: int
    gender: str
    blood_group: str
    city: str
    phone_number: int
