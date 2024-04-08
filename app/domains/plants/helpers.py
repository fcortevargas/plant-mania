from http import HTTPStatus

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.models.plant import Plant
from app.dependencies import get_session


def get_plant_by_id(
        plant_id: int,
        db_session: Session = Depends(get_session)
) -> Plant:
    user = db_session.query(Plant).filter(Plant.id == plant_id).one_or_none()

    if not user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail=f"Plant with ID={plant_id} not found."
        )

    return user
