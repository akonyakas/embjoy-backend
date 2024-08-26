from pydantic import BaseModel
from enum import Enum


class MedConditionsEnum(str, Enum):
    diabetes = 'diabetes'
    high_blood_pressure = 'high blood pressure'
    asthma = 'asthma'
    fertility_issues = 'fertility issues'
    mental_health_conditions = 'mental health conditions'
    obesity = 'obesity'
    other = 'other'


class UserBase(BaseModel):
    username: str
    role: str
    days_pregnant: int
    num_of_pregnancies: int
    num_of_failed_pregnancies: int
    first_time_pregnancy: bool
    prev_failed_pregnancies: bool
    med_conditions: MedConditionsEnum


class UserCreate(UserBase):
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class UserOut(UserBase):
    id: int

    class Config:
        from_attributes = True
