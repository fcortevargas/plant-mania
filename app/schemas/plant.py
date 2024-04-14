from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel


class PlantBase(BaseModel):
    name: str
    room_id: int
    date_last_watered: Optional[date] = None
    date_last_repotted: Optional[date] = None
    date_last_fertilized: Optional[date] = None


class PlantCreate(PlantBase):
    species_id: int


class PlantUpdate(PlantBase):
    name: Optional[str] = None
    room_id: Optional[int] = None


class PlantOut(PlantBase):
    id: int
    species_id: int
    created_timestamp: datetime
    updated_timestamp: datetime
