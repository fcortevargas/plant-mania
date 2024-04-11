from datetime import date
from typing import Optional

from pydantic import BaseModel


class PlantBase(BaseModel):
    name: str
    location_in_house: str
    species_id: int
    user_id: int


class PlantCreate(PlantBase):
    pass


class PlantUpdate(PlantBase):
    name: Optional[str] = None
    location_in_house: Optional[str] = None
    species_id: Optional[int] = None
    date_last_watered: Optional[date] = None
    user_id: Optional[int] = None


class PlantOut(PlantBase):
    id: int
    date_last_watered: Optional[date] = None
