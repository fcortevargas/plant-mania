from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.models.plant import Plant
from app.database.models.species import Species
from app.dependencies import get_session
from app.domains.plants.helpers import get_plant_by_id, raise_not_found_error
from app.domains.species.helpers import get_species_by_id
from app.schemas.plant import PlantCreate, PlantOut, PlantUpdate

plant_router = APIRouter(prefix="/plants", tags=["plants"])


@plant_router.post("", response_model=PlantOut)
def create_plant(
        plant_create: PlantCreate,
        db_session: Session = Depends(get_session)
) -> PlantOut:
    get_species_by_id(plant_create.species_id, db_session)

    new_plant = Plant(**plant_create.model_dump())

    db_session.add(new_plant)
    db_session.commit()
    db_session.refresh(new_plant)

    return new_plant


@plant_router.get("", response_model=List[PlantOut])
def get_all_plants(db_session: Session = Depends(get_session)) -> List[PlantOut]:
    plants = db_session.query(Plant).all()
    return plants


@plant_router.get("/{plant_id}", response_model=PlantOut)
def get_plant(
        plant_id: int,
        db_session: Session = Depends(get_session)
) -> PlantOut:
    return get_plant_by_id(plant_id, db_session)


@plant_router.get("/species/{species_name}", response_model=List[PlantOut])
def get_all_plant_by_species(
        species_name: str,
        db_session: Session = Depends(get_session)
) -> List[PlantOut]:
    species = db_session.query(Species).filter(Species.name == species_name).one_or_none()

    raise_not_found_error(species, f"Species with NAME={species_name} not found.")

    plants = db_session.query(Plant).filter(Plant.species_id == species.id).all()

    return plants


@plant_router.patch("/{plant_id}")
def update_user(
        plant_id: int,
        plant_update: PlantUpdate,
        db_session: Session = Depends(get_session)
) -> PlantOut:
    plant = get_plant_by_id(plant_id, db_session)

    for key, value in plant_update.model_dump().items():
        if value:
            setattr(plant, key, value)

    db_session.commit()

    return plant


@plant_router.delete("/{plant_id}", response_model=PlantOut)
def delete_plant(
        plant_id: int,
        db_session: Session = Depends(get_session)
) -> PlantOut:
    plant = get_plant_by_id(plant_id, db_session)

    db_session.delete(plant)
    db_session.commit()

    return plant
