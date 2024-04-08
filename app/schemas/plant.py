from typing import Optional

from pydantic import BaseModel


class PlantBase(BaseModel):
    name: str
    location: str
    species_id: int


class PlantCreate(PlantBase):
    pass


class PlantUpdate(PlantBase):
    name: Optional[str] = None
    location: Optional[str] = None
    species_id: Optional[int] = None


class PlantOut(PlantBase):
    id: int
