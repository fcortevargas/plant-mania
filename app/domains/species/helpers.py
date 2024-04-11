from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.models.plant import Species
from app.dependencies import get_session
from app.domains.helpers import raise_not_found_error


def get_species_by_id(
        species_id: int,
        db_session: Session = Depends(get_session)
) -> Species:
    species = db_session.query(Species).filter(Species.id == species_id).one_or_none()

    raise_not_found_error(species, f"Species with ID={species_id} not found.")

    return species
