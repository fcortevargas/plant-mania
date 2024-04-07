from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    first_name: str
    last_name: str


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    username: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    password: Optional[str] = None


class UserOut(UserBase):
    id: int
    created_timestamp: datetime
    updated_timestamp: datetime
