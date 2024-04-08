import sqlalchemy as sa

from app.database.base import Base


class Species(Base):
    __tablename__ = "species"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True, nullable=False, index=True)
    name = sa.Column(sa.String, nullable=False, unique=True)
    country = sa.Column(sa.String, nullable=True)
    water_frequency = sa.Column(sa.Integer, nullable=False)
    lighting = sa.Column(sa.String, nullable=False)
