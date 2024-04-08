from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.models.user import User
from app.dependencies import get_session
from app.domains.users.helpers import get_user_by_id
from app.schemas.user import UserCreate, UserOut, UserUpdate

user_router = APIRouter(prefix="/users", tags=["users"])


@user_router.post("", response_model=UserOut)
def create_user(
        user_create: UserCreate,
        db_session: Session = Depends(get_session)
) -> UserOut:
    new_user = User(**user_create.model_dump())

    db_session.add(new_user)
    db_session.commit()
    db_session.refresh(new_user)

    return new_user


@user_router.patch("/{user_id}")
def update_user(
        user_id: int,
        user_update: UserUpdate,
        db_session: Session = Depends(get_session)
) -> UserOut:
    user = get_user_by_id(user_id, db_session)

    for key, value in user_update.model_dump().items():
        if value:
            setattr(user, key, value)

    db_session.commit()

    return user


@user_router.get("", response_model=List[UserOut])
def get_all_users(db_session: Session = Depends(get_session)) -> List[UserOut]:
    users = db_session.query(User).all()
    return users


@user_router.get("/{user_id}", response_model=UserOut)
def get_user(
        user_id: int,
        db_session: Session = Depends(get_session)
) -> UserOut:
    return get_user_by_id(user_id, db_session)


@user_router.delete("/{user_id}", response_model=UserOut)
def delete_user(
        user_id: int,
        db_session: Session = Depends(get_session)
) -> UserOut:
    user = get_user_by_id(user_id, db_session)

    db_session.delete(user)
    db_session.commit()

    return user
