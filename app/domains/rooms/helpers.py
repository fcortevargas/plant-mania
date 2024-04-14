from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.models.room import Room
from app.dependencies import get_session
from app.domains.helpers import raise_not_found_error


def get_room_by_id(
        room_id: int,
        db_session: Session = Depends(get_session)
) -> Room:
    room = db_session.query(Room).filter(Room.id == room_id).one_or_none()

    raise_not_found_error(room, f"Room with ID={room_id} not found.")

    return room
