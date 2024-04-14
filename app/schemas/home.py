from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class HomeBase(BaseModel):
    name: str


class HomeCreate(HomeBase):
    pass


class HomeUpdate(HomeBase):
    name: Optional[str] = None


class HomeOut(HomeBase):
    id: int
    created_timestamp: datetime
    updated_timestamp: datetime
