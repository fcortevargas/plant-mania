from typing import Optional

from pydantic import BaseModel


class RoomBase(BaseModel):
    name: str


class RoomCreate(RoomBase):
    home_id: int
    floor_plan: Optional[bytes] = None


class RoomUpdate(RoomBase):
    name: Optional[str] = None
    floor_plan: Optional[bytes] = None


class RoomOut(RoomBase):
    id: int
