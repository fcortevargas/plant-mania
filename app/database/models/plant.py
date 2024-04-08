import sqlalchemy as sa
from sqlalchemy.orm import backref, relationship

from app.database.base import Base
from app.database.models.species import Species


class Plant(Base):
    __tablename__ = "plants"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True, nullable=False, index=True)
    name = sa.Column(sa.String, nullable=True, unique=True)
    location = sa.Column(sa.String, nullable=False)
    species_id = sa.Column(sa.Integer, sa.ForeignKey("species.id"), nullable=False)
    species = relationship(Species, backref=backref("plants", cascade="all, delete-orphan"))
