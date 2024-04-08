from typing import Optional

from pydantic import BaseModel


class SpeciesBase(BaseModel):
    name: str
    country: Optional[str]
    water_frequency: int
    lighting: str


class SpeciesCreate(SpeciesBase):
    pass


class SpeciesUpdate(SpeciesBase):
    name: Optional[str] = None
    country: Optional[str] = None
    water_frequency: Optional[int] = None
    lighting: Optional[str] = None


class SpeciesOut(SpeciesBase):
    id: int
