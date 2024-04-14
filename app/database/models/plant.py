import sqlalchemy as sa
from sqlalchemy.orm import backref, relationship

from app.database.base import Base
from app.database.models.room import Room
from app.database.models.species import Species


class Plant(Base):
    __tablename__ = "plants"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True, nullable=False, index=True, unique=True)
    species_id = sa.Column(sa.Integer, sa.ForeignKey("species.id"), nullable=False)
    species = relationship(Species, backref=backref("plants", cascade="all, delete-orphan"))
    name = sa.Column(sa.String, nullable=True)
    room_id = sa.Column(sa.Integer, sa.ForeignKey("rooms.id"), nullable=False)
    room = relationship(Room, backref=backref("plants", cascade="all, delete-orphan"))
    date_last_watered = sa.Column(sa.Date, nullable=True)
    date_last_repotted = sa.Column(sa.Date, nullable=True)
    date_last_fertilized = sa.Column(sa.Date, nullable=True)
    created_timestamp = sa.Column(sa.DateTime, nullable=False, server_default=sa.func.now())
    updated_timestamp = sa.Column(sa.DateTime, nullable=False, server_default=sa.func.now())
