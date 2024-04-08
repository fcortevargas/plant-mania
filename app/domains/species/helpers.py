from http import HTTPStatus

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.models.plant import Species
from app.dependencies import get_session


def get_species_by_id(
        species_id: int,
        db_session: Session = Depends(get_session)
) -> Species:
    user = db_session.query(Species).filter(Species.id == species_id).one_or_none()

    if not user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail=f"Species with ID={species_id} not found."
        )

    return user
