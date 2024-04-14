import sqlalchemy as sa
from sqlalchemy.orm import relationship, backref

from app.database.base import Base
from app.database.models.home import Home


class Room(Base):
    __tablename__ = "rooms"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True, nullable=False, index=True, unique=True)
    home_id = sa.Column(sa.Integer, sa.ForeignKey("homes.id"), nullable=False)
    home = relationship(Home, backref=backref("rooms", cascade="all, delete-orphan"))
    name = sa.Column(sa.String, nullable=False)
    floor_plan = sa.Column(sa.LargeBinary, nullable=True)
