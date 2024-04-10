"""create plants table

Revision ID: 5f9fd3b03e90
Revises: 6a02bbb960cd
Create Date: 2024-04-05 21:24:42.179141

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '5f9fd3b03e90'
down_revision = '6a02bbb960cd'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "species",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True, nullable=False, index=True),
        sa.Column("name", sa.String, nullable=False, unique=True),
        sa.Column("country", sa.String, nullable=True),
        sa.Column("watering_interval", sa.Integer, nullable=False),
        sa.Column("lighting_conditions", sa.String, nullable=False)
    )

    op.create_table(
        "plants",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True, nullable=False, index=True),
        sa.Column("name", sa.String, nullable=True),
        sa.Column("location_in_house", sa.String, nullable=False),
        sa.Column("species_id", sa.Integer, sa.ForeignKey("species.id"), nullable=False)
    )


def downgrade() -> None:
    op.drop_table("plants")
    op.drop_table("species")
