"""populate tables

Revision ID: a34ba483ce97
Revises: 5f9fd3b03e90
Create Date: 2024-04-10 23:21:46.608591

"""

import datetime

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'a34ba483ce97'
down_revision = '5f9fd3b03e90'
branch_labels = None
depends_on = None


def upgrade() -> None:
    species_table = sa.table(
        "species",
        sa.Column("name", sa.String),
        sa.Column("country", sa.String),
        sa.Column("watering_interval", sa.Integer),
        sa.Column("lighting_conditions", sa.String)
    )

    op.bulk_insert(
        species_table,
        [
            {"name": "Monstera Deliciosa", "country": "Mexico", "watering_interval": 7,
             "lighting_conditions": "Bright Indirect"},
            {"name": "Chamaedorea Elegans", "country": "Mexico", "watering_interval": 7,
             "lighting_conditions": "Bright Indirect"},
            {"name": "Ctenanthe", "country": "Brazil", "watering_interval": 5,
             "lighting_conditions": "Medium"},
            {"name": "Calathea Insignis", "country": "Brazil", "watering_interval": 7,
             "lighting_conditions": "Bright Indirect"},
            {"name": "Spathiphyllum", "country": "Mexico", "watering_interval": 4,
             "lighting_conditions": "Bright Indirect"},
            {"name": "Kroenleinia Grusonii", "country": "Mexico", "watering_interval": 60,
             "lighting_conditions": "Bright Direct"},
            {"name": "Maranta Leuconeura", "country": "Brazil", "watering_interval": 7,
             "lighting_conditions": "Bright Indirect"},
            {"name": "Ananas Comosus", "country": "Brazil", "watering_interval": 15,
             "lighting_conditions": "Bright Direct"},
            {"name": "Beaucarnea Recurvata", "country": "Mexico", "watering_interval": 10,
             "lighting_conditions": "Bright Indirect"},
            {"name": "Peperomia Rotundifolia", "country": "Brazil", "watering_interval": 15,
             "lighting_conditions": "Bright Direct"},
            {"name": "Yucca", "country": "Mexico", "watering_interval": 15,
             "lighting_conditions": "Bright Direct"},
            {"name": "Aeschynanthus Radicans", "country": "Indonesia", "watering_interval": 7,
             "lighting_conditions": "Bright Indirect"},
            {"name": "Hypoestes Phyllostachya", "country": "Madagascar", "watering_interval": 3,
             "lighting_conditions": "Medium"},
            {"name": "Zamioculcas Zamiifolia", "country": "Kenya", "watering_interval": 15,
             "lighting_conditions": "Bright Indirect"},
            {"name": "Sansevieria Trifasciata", "country": "Nigeria", "watering_interval": 15,
             "lighting_conditions": "Bright Indirect"},
            {"name": "Persea Americana", "country": "Mexico", "watering_interval": 7,
             "lighting_conditions": "Bright Direct"}
        ]
    )

    plants_table = sa.table(
        "plants",
        sa.Column("name", sa.String),
        sa.Column("location_in_house", sa.String),
        sa.Column("species_id", sa.Integer)
    )

    op.bulk_insert(
        plants_table,
        [
            {"name": "Monstera", "location_in_house": "Living Room", "species_id": 1},
            {"name": "Parlour Palm", "location_in_house": "Living Room", "species_id": 2},
            {"name": "Ctenanthe", "location_in_house": "Living Room", "species_id": 3},
            {"name": "Ctenanthe", "location_in_house": "Office", "species_id": 3},
            {"name": "Rattlesnake Plant", "location_in_house": "Living Room", "species_id": 4},
            {"name": "Peace Lily", "location_in_house": "Living Room", "species_id": 5},
            {"name": "Golden Barrel Cactus", "location_in_house": "Living Room", "species_id": 6},
            {"name": "Prayer Plant", "location_in_house": "Living Room", "species_id": 7},
            {"name": "Pineapple", "location_in_house": "Living Room", "species_id": 8},
            {"name": "Elephant's Foot", "location_in_house": "Living Room", "species_id": 9},
            {"name": "Jade Necklace", "location_in_house": "Living Room", "species_id": 10},
            {"name": "Yucca", "location_in_house": "Living Room", "species_id": 11},
            {"name": "Lipstick Plant", "location_in_house": "Living Room", "species_id": 12},
            {"name": "Polka Dot Plant", "location_in_house": "Living Room", "species_id": 13},
            {"name": "Eternity Plant", "location_in_house": "Living Room", "species_id": 14},
            {"name": "Snake Plant", "location_in_house": "Living Room", "species_id": 15},
            {"name": "Avocado", "location_in_house": "Living Room", "species_id": 16}
        ]
    )

    users_table = sa.table(
        "users",
        sa.Column("username", sa.String),
        sa.Column("first_name", sa.String),
        sa.Column("last_name", sa.String),
        sa.Column("password", sa.String),
        sa.Column("created_timestamp", sa.DateTime),
        sa.Column("updated_timestamp", sa.DateTime)
    )

    op.bulk_insert(
        users_table,
        [
            {"username": "fcortevargas", "first_name": "Fernando", "last_name": "Corte Vargas", "password": "pass",
             "created_timestamp": datetime.datetime.utcnow(), "updated_timestamp": datetime.datetime.utcnow()},
            {"username": "jpinhoferreira", "first_name": "João", "last_name": "Pinho Ferreira", "password": "pass",
             "created_timestamp": datetime.datetime.utcnow(), "updated_timestamp": datetime.datetime.utcnow()}
        ]
    )


def downgrade() -> None:
    pass
