from typing import Optional

from pydantic import BaseModel


class PlantLocationBase(BaseModel):
    plant_id: int
    room_id: int
    x_pos: float
    y_pos: float


class PlantLocationCreate(PlantLocationBase):
    pass


class PlantLocationUpdate(PlantLocationBase):
    x_pos: Optional[float] = None
    y_pos: Optional[float] = None


class PlantLocationOut(PlantLocationBase):
    pass
