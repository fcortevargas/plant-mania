from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.models.room import Room
from app.dependencies import get_session
from app.domains.rooms.helpers import get_room_by_id
from app.schemas.room import RoomCreate, RoomOut, RoomUpdate

room_router = APIRouter(prefix="/rooms", tags=["rooms"])


@room_router.post("", response_model=RoomOut)
def create_room(
        room_create: RoomCreate,
        db_session: Session = Depends(get_session)
) -> RoomOut:
    new_room = Room(**room_create.model_dump())

    db_session.add(new_room)
    db_session.commit()
    db_session.refresh(new_room)

    return new_room


@room_router.get("", response_model=List[RoomOut])
def get_all_rooms(db_session: Session = Depends(get_session)) -> List[RoomOut]:
    rooms = db_session.query(Room).all()
    return rooms


@room_router.get("/{room_id}", response_model=RoomOut)
def get_room(
        room_id: int,
        db_session: Session = Depends(get_session)
) -> RoomOut:
    return get_room_by_id(room_id, db_session)


@room_router.patch("/{room_id}")
def update_room(
        room_id: int,
        room_update: RoomUpdate,
        db_session: Session = Depends(get_session)
) -> RoomOut:
    room = get_room_by_id(room_id, db_session)

    for key, value in room_update.model_dump().items():
        if value:
            setattr(room, key, value)

    db_session.commit()

    return room


@room_router.delete("/{room_id}", response_model=RoomOut)
def delete_room(
        room_id: int,
        db_session: Session = Depends(get_session)
) -> RoomOut:
    room = get_room_by_id(room_id, db_session)

    db_session.delete(room)
    db_session.commit()

    return room
