from http import HTTPStatus

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.models.user import User
from app.dependencies import get_session
from app.schemas.user import UserOut


def get_user_by_id(
        user_id: int,
        db_session: Session = Depends(get_session)
) -> User:
    user = db_session.query(User).filter(User.id == user_id).one_or_none()

    if not user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail=f"User with ID={user_id} not found."
        )

    return user
