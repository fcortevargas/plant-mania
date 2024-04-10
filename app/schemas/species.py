from typing import Optional

from pydantic import BaseModel


class SpeciesBase(BaseModel):
    name: str
    country: Optional[str]
    watering_interval: int
    lighting_conditions: str


class SpeciesCreate(SpeciesBase):
    pass


class SpeciesUpdate(SpeciesBase):
    name: Optional[str] = None
    country: Optional[str] = None
    watering_interval: Optional[int] = None
    lighting_conditions: Optional[str] = None


class SpeciesOut(SpeciesBase):
    id: int
