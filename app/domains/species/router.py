from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.models.species import Species
from app.dependencies import get_session
from app.schemas.species import SpeciesCreate, SpeciesOut

species_router = APIRouter(prefix="/species", tags=["species"])


@species_router.post("", response_model=SpeciesOut)
def create_species(
        species_create: SpeciesCreate,
        db_session: Session = Depends(get_session)
) -> SpeciesOut:
    new_species = Species(**species_create.model_dump())

    db_session.add(new_species)
    db_session.commit()
    db_session.refresh(new_species)

    return new_species
