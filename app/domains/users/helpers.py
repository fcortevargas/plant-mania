from http import HTTPStatus

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.models.user import User
from app.dependencies import get_session


def get_user_by_id(
        user_id: int,
        db_session: Session = Depends(get_session)
) -> User:
    user = db_session.query(User).filter(User.id == user_id).one_or_none()

    raise_not_found_error(user, f"User with ID={user_id} not found.")

    return user


def raise_not_found_error(query, message):
    if not query:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail=message
        )
