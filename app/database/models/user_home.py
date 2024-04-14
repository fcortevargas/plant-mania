import sqlalchemy as sa
from sqlalchemy.orm import relationship, backref

from app.database.base import Base
from app.database.models.home import Home
from app.database.models.user import User


class UserHome(Base):
    __tablename__ = "user_homes"

    user_id = sa.Column(sa.Integer, sa.ForeignKey("users.id"), nullable=False)
    user = relationship(User, backref=backref("user_homes", cascade="all, delete-orphan"))
    home_id = sa.Column(sa.Integer, sa.ForeignKey("homes.id"), nullable=False)
    home = relationship(Home, backref=backref("user_homes", cascade="all, delete-orphan"))
