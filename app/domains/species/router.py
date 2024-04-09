from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.models.species import Species
from app.dependencies import get_session
from app.domains.species.helpers import get_species_by_id
from app.schemas.species import SpeciesCreate, SpeciesOut, SpeciesUpdate

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


@species_router.get("", response_model=List[SpeciesOut])
def get_all_species(db_session: Session = Depends(get_session)) -> List[SpeciesOut]:
    species = db_session.query(Species).all()
    return species


@species_router.get("/{species_id}", response_model=SpeciesOut)
def get_species(
        species_id: int,
        db_session: Session = Depends(get_session)
) -> SpeciesOut:
    return get_species_by_id(species_id, db_session)


@species_router.patch("/{species_id}")
def update_species(
        species_id: int,
        species_update: SpeciesUpdate,
        db_session: Session = Depends(get_session)
) -> SpeciesOut:
    species = get_species_by_id(species_id, db_session)

    for key, value in species_update.model_dump().items():
        if value:
            setattr(species, key, value)

    db_session.commit()

    return species


@species_router.delete("/{species_id}", response_model=SpeciesOut)
def delete_species(
        species_id: int,
        db_session: Session = Depends(get_session)
) -> SpeciesOut:
    species = get_species_by_id(species_id, db_session)

    db_session.delete(species)
    db_session.commit()

    return species
