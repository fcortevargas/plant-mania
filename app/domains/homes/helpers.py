from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.models.home import Home
from app.dependencies import get_session
from app.domains.helpers import raise_not_found_error


def get_home_by_id(
        home_id: int,
        db_session: Session = Depends(get_session)
) -> Home:
    home = db_session.query(Home).filter(Home.id == home_id).one_or_none()

    raise_not_found_error(home, f"Home with ID={home_id} not found.")

    return home
