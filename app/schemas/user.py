from datetime import datetime, date
from typing import Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    first_name: str
    last_name: str


class UserCreate(UserBase):
    birth_date: date
    password: str


class UserUpdate(UserBase):
    username: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    password: Optional[str] = None


class UserOut(UserBase):
    id: int
    birth_date: date
    created_timestamp: datetime
    updated_timestamp: datetime
