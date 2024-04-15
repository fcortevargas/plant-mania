from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.models.home import Home
from app.dependencies import get_session
from app.domains.homes.helpers import get_home_by_id
from app.schemas.home import HomeCreate, HomeOut, HomeUpdate

home_router = APIRouter(prefix="/homes", tags=["homes"])


@home_router.post("", response_model=HomeOut)
def create_home(
        home_create: HomeCreate,
        db_session: Session = Depends(get_session)
) -> HomeOut:
    new_home = Home(**home_create.model_dump())

    db_session.add(new_home)
    db_session.commit()
    db_session.refresh(new_home)

    return new_home


@home_router.get("", response_model=List[HomeOut])
def get_all_homes(db_session: Session = Depends(get_session)) -> List[HomeOut]:
    homes = db_session.query(Home).all()
    return homes


@home_router.get("/{home_id}", response_model=HomeOut)
def get_home(
        home_id: int,
        db_session: Session = Depends(get_session)
) -> HomeOut:
    return get_home_by_id(home_id, db_session)


@home_router.patch("/{home_id}")
def update_home(
        home_id: int,
        home_update: HomeUpdate,
        db_session: Session = Depends(get_session)
) -> HomeOut:
    home = get_home_by_id(home_id, db_session)

    for key, value in home_update.model_dump().items():
        if value:
            setattr(home, key, value)

    db_session.commit()

    return home


@home_router.delete("/{home_id}", response_model=HomeOut)
def delete_home(
        home_id: int,
        db_session: Session = Depends(get_session)
) -> HomeOut:
    home = get_home_by_id(home_id, db_session)

    db_session.delete(home)
    db_session.commit()

    return home
