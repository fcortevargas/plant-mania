import sqlalchemy as sa

from app.database.base import Base


class Home(Base):
    __tablename__ = "homes"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True, nullable=False, index=True, unique=True)
    name = sa.Column(sa.String, nullable=False)
    created_timestamp = sa.Column(sa.DateTime, nullable=False, server_default=sa.func.now())
    updated_timestamp = sa.Column(sa.DateTime, nullable=False, server_default=sa.func.now())
