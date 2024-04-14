import sqlalchemy as sa
from sqlalchemy.orm import backref, relationship

from app.database.base import Base
from app.database.models.plant import Plant
from app.database.models.room import Room


class PlantLocation(Base):
    __tablename__ = "plant_locations"

    plant_id = sa.Column(sa.Integer, nullable=False)
    plant = relationship(Plant, backref=backref("plant_locations", cascade="all, delete-orphan"))
    room_id = sa.Column(sa.Integer, nullable=False)
    room = relationship(Room, backref=backref("plant_locations", cascade="all, delete-orphan"))
    x_pos = sa.Column(sa.Float, nullable=False)
    y_pos = sa.Column(sa.Float, nullable=False)
