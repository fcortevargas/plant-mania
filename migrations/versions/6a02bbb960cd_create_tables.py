"""Create users table

Revision ID: 6a02bbb960cd
Revises: 
Create Date: 2023-03-26 16:53:25.430495

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '6a02bbb960cd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True, nullable=False, index=True),
        sa.Column("username", sa.String, nullable=False, unique=True),
        sa.Column("password", sa.String, nullable=False),
        sa.Column("first_name", sa.String, nullable=False),
        sa.Column("last_name", sa.String, nullable=False),
        sa.Column("birth_date", sa.Date, nullable=False),
        sa.Column("created_timestamp", sa.DateTime, nullable=False, server_default=sa.func.now()),
        sa.Column("updated_timestamp", sa.DateTime, nullable=False, server_default=sa.func.now())
    )

    op.create_table(
        "homes",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True, nullable=False, index=True, unique=True),
        sa.Column("name", sa.String, nullable=False),
        sa.Column("created_timestamp", sa.DateTime, nullable=False, server_default=sa.func.now()),
        sa.Column("updated_timestamp", sa.DateTime, nullable=False, server_default=sa.func.now())
    )

    op.create_table(
        "user_homes",
        sa.Column("user_id", sa.Integer, nullable=False),
        sa.Column("home_id", sa.Integer, nullable=False),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["home_id"], ["homes.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("user_id", "home_id")
    )

    op.create_table(
        "rooms",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True, nullable=False, index=True, unique=True),
        sa.Column("home_id", sa.Integer, nullable=False),
        sa.Column("name", sa.String, nullable=False),
        sa.Column("floor_plan", sa.LargeBinary, nullable=True),
        sa.ForeignKeyConstraint(["home_id"], ["homes.id"], ondelete="CASCADE")
    )

    op.create_table(
        "species",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True, nullable=False, index=True, unique=True),
        sa.Column("name", sa.String, nullable=False, unique=True),
        sa.Column("country", sa.String, nullable=True),
        sa.Column("watering_interval", sa.Integer, nullable=False),
        sa.Column("lighting_conditions", sa.String, nullable=False)
    )

    op.create_table(
        "plants",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True, nullable=False, index=True, unique=True),
        sa.Column("species_id", sa.Integer, nullable=False),
        sa.Column("name", sa.String, nullable=True),
        sa.Column("room_id", sa.Integer, nullable=False),
        sa.Column("date_last_watered", sa.Date, nullable=True),
        sa.Column("date_last_repotted", sa.Date, nullable=True),
        sa.Column("date_last_fertilized", sa.Date, nullable=True),
        sa.Column("created_timestamp", sa.DateTime, nullable=False, server_default=sa.func.now()),
        sa.Column("updated_timestamp", sa.DateTime, nullable=False, server_default=sa.func.now()),
        sa.ForeignKeyConstraint(["species_id"], ["species.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["room_id"], ["rooms.id"], ondelete="CASCADE"),
    )

    op.create_table(
        "plant_locations",
        sa.Column("plant_id", sa.Integer, nullable=False),
        sa.Column("room_id", sa.Integer, nullable=False),
        sa.Column("x_pos", sa.Float, nullable=False),
        sa.Column("y_pos", sa.Float, nullable=False),
        sa.ForeignKeyConstraint(["plant_id"], ["plants.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["room_id"], ["rooms.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("plant_id", "room_id")
    )


def downgrade() -> None:
    op.drop_table("plant_locations")
    op.drop_table("plants")
    op.drop_table("species")
    op.drop_table("rooms")
    op.drop_table("user_homes")
    op.drop_table("homes")
    op.drop_table("users")
