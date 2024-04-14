"""populate tables

Revision ID: a34ba483ce97
Revises: 5f9fd3b03e90
Create Date: 2024-04-10 23:21:46.608591

"""

from datetime import date, datetime

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'a34ba483ce97'
down_revision = '6a02bbb960cd'
branch_labels = None
depends_on = None


def upgrade() -> None:
    users_table = sa.table(
        "users",
        sa.Column("username", sa.String),
        sa.Column("first_name", sa.String),
        sa.Column("last_name", sa.String),
        sa.Column("password", sa.String),
        sa.Column("created_timestamp", sa.DateTime),
        sa.Column("updated_timestamp", sa.DateTime),
        sa.Column("birth_date", sa.Date)
    )

    op.bulk_insert(
        users_table,
        [
            {"username": "fcortevargas", "first_name": "Fernando", "last_name": "Corte Vargas", "password": "pass",
             "created_timestamp": datetime.utcnow(), "updated_timestamp": datetime.utcnow(),
             "birth_date": date(1997, 6, 3)},
            {"username": "jpinhoferreira", "first_name": "João", "last_name": "Pinho Ferreira", "password": "pass",
             "created_timestamp": datetime.utcnow(), "updated_timestamp": datetime.utcnow(),
             "birth_date": date(1997, 9, 22)},
        ]
    )

    homes = sa.table(
        "homes",
        sa.Column("name", sa.String),
        sa.Column("created_timestamp", sa.DateTime),
        sa.Column("updated_timestamp", sa.DateTime)
    )

    op.bulk_insert(
        homes,
        [
            {"name": "Joãonando", "created_timestamp": datetime.utcnow(), "updated_timestamp": datetime.utcnow()}
        ]
    )

    user_homes = sa.table(
        "user_homes",
        sa.Column("user_id", sa.Integer),
        sa.Column("home_id", sa.Integer)
    )

    op.bulk_insert(
        user_homes,
        [
            {"user_id": 1, "home_id": 1},
            {"user_id": 2, "home_id": 1}
        ]
    )

    rooms = sa.table(
        "rooms",
        sa.Column("home_id", sa.Integer),
        sa.Column("name", sa.String),
        sa.Column("floor_plan", sa.LargeBinary, nullable=True)
    )

    op.bulk_insert(
        rooms,
        [
            {"home_id": 1, "name": "Living Room"},
            {"home_id": 1, "name": "Office"}
        ]
    )

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
        sa.Column("species_id", sa.Integer),
        sa.Column("name", sa.String),
        sa.Column("room_id", sa.Integer),
        sa.Column("date_last_watered", sa.Date),
        sa.Column("date_last_repotted", sa.Date),
        sa.Column("date_last_fertilized", sa.Date),
        sa.Column("created_timestamp", sa.DateTime),
        sa.Column("updated_timestamp", sa.DateTime)
    )

    op.bulk_insert(
        plants_table,
        [
            {"species_id": 1, "name": "Monstera", "room_id": 1, "date_last_watered": date(2024, 4, 3),
             "date_last_repotted": date(2023, 2, 5), "date_last_fertilized": date(2023, 8, 10),
             "created_timestamp": datetime.utcnow(), "updated_timestamp": datetime.utcnow()},
            {"species_id": 2, "name": "Parlour Palm", "room_id": 1, "date_last_watered": date(2024, 4, 3),
             "date_last_repotted": date(2023, 2, 5), "date_last_fertilized": date(2023, 8, 10),
             "created_timestamp": datetime.utcnow(), "updated_timestamp": datetime.utcnow()},
            {"species_id": 3, "name": "Ctenanthe", "room_id": 1, "date_last_watered": date(2024, 4, 3),
             "date_last_repotted": date(2023, 2, 5), "date_last_fertilized": date(2023, 8, 10),
             "created_timestamp": datetime.utcnow(), "updated_timestamp": datetime.utcnow()},
            {"species_id": 3, "name": "Ctenanthe", "room_id": 2, "date_last_watered": date(2024, 4, 3),
             "date_last_repotted": date(2023, 2, 5), "date_last_fertilized": date(2023, 8, 10),
             "created_timestamp": datetime.utcnow(), "updated_timestamp": datetime.utcnow()},
            {"species_id": 4, "name": "Rattlesnake Plant", "room_id": 1, "date_last_watered": date(2024, 4, 3),
             "date_last_repotted": date(2023, 2, 5), "date_last_fertilized": date(2023, 8, 10),
             "created_timestamp": datetime.utcnow(), "updated_timestamp": datetime.utcnow()},
            {"species_id": 5, "name": "Peace Lily", "room_id": 1, "date_last_watered": date(2024, 4, 3),
             "date_last_repotted": date(2023, 2, 5), "date_last_fertilized": date(2023, 8, 10),
             "created_timestamp": datetime.utcnow(), "updated_timestamp": datetime.utcnow()},
            {"species_id": 6, "name": "Golden Barrel Cactus", "room_id": 1, "date_last_watered": date(2024, 4, 3),
             "date_last_repotted": date(2023, 2, 5), "date_last_fertilized": date(2023, 8, 10),
             "created_timestamp": datetime.utcnow(), "updated_timestamp": datetime.utcnow()},
            {"species_id": 7, "name": "Prayer Plant", "room_id": 1, "date_last_watered": date(2024, 4, 3),
             "date_last_repotted": date(2023, 2, 5), "date_last_fertilized": date(2023, 8, 10),
             "created_timestamp": datetime.utcnow(), "updated_timestamp": datetime.utcnow()},
            {"species_id": 8, "name": "Pineapple", "room_id": 1, "date_last_watered": date(2024, 4, 3),
             "date_last_repotted": date(2023, 2, 5), "date_last_fertilized": date(2023, 8, 10),
             "created_timestamp": datetime.utcnow(), "updated_timestamp": datetime.utcnow()},
            {"species_id": 9, "name": "Elephant's Foot", "room_id": 1, "date_last_watered": date(2024, 4, 3),
             "date_last_repotted": date(2023, 2, 5), "date_last_fertilized": date(2023, 8, 10),
             "created_timestamp": datetime.utcnow(), "updated_timestamp": datetime.utcnow()},
            {"species_id": 10, "name": "Jade Necklace", "room_id": 1, "date_last_watered": date(2024, 4, 3),
             "date_last_repotted": date(2023, 2, 5), "date_last_fertilized": date(2023, 8, 10),
             "created_timestamp": datetime.utcnow(), "updated_timestamp": datetime.utcnow()},
            {"species_id": 11, "name": "Yucca", "room_id": 1, "date_last_watered": date(2024, 4, 3),
             "date_last_repotted": date(2023, 2, 5), "date_last_fertilized": date(2023, 8, 10),
             "created_timestamp": datetime.utcnow(), "updated_timestamp": datetime.utcnow()},
            {"species_id": 12, "name": "Lipstick Plant", "room_id": 1, "date_last_watered": date(2024, 4, 3),
             "date_last_repotted": date(2023, 2, 5), "date_last_fertilized": date(2023, 8, 10),
             "created_timestamp": datetime.utcnow(), "updated_timestamp": datetime.utcnow()},
            {"species_id": 13, "name": "Polka Dot Plant", "room_id": 1, "date_last_watered": date(2024, 4, 3),
             "date_last_repotted": date(2023, 2, 5), "date_last_fertilized": date(2023, 8, 10),
             "created_timestamp": datetime.utcnow(), "updated_timestamp": datetime.utcnow()},
            {"species_id": 14, "name": "Eternity Plant", "room_id": 1, "date_last_watered": date(2024, 4, 3),
             "date_last_repotted": date(2023, 2, 5), "date_last_fertilized": date(2023, 8, 10),
             "created_timestamp": datetime.utcnow(), "updated_timestamp": datetime.utcnow()},
            {"species_id": 15, "name": "Snake Plant", "room_id": 1, "date_last_watered": date(2024, 4, 3),
             "date_last_repotted": date(2023, 2, 5), "date_last_fertilized": date(2023, 8, 10),
             "created_timestamp": datetime.utcnow(), "updated_timestamp": datetime.utcnow()},
            {"species_id": 16, "name": "Avocado", "room_id": 1, "date_last_watered": date(2024, 4, 3),
             "date_last_repotted": date(2023, 2, 5), "date_last_fertilized": date(2023, 8, 10),
             "created_timestamp": datetime.utcnow(), "updated_timestamp": datetime.utcnow()},
        ]
    )

    plant_locations = sa.table(
        "plant_locations",
        sa.Column("plant_id", sa.Integer),
        sa.Column("room_id", sa.Integer),
        sa.Column("x_pos", sa.Float),
        sa.Column("y_pos", sa.Float)
    )

    op.bulk_insert(
        plant_locations,
        [
            {"plant_id": 1, "room_id": 1, "x_pos": 0, "y_pos": 0},
            {"plant_id": 2, "room_id": 1, "x_pos": 0, "y_pos": 0},
            {"plant_id": 3, "room_id": 1, "x_pos": 0, "y_pos": 0},
            {"plant_id": 4, "room_id": 2, "x_pos": 0, "y_pos": 0},
            {"plant_id": 5, "room_id": 1, "x_pos": 0, "y_pos": 0},
            {"plant_id": 6, "room_id": 1, "x_pos": 0, "y_pos": 0},
            {"plant_id": 7, "room_id": 1, "x_pos": 0, "y_pos": 0},
            {"plant_id": 8, "room_id": 1, "x_pos": 0, "y_pos": 0},
            {"plant_id": 9, "room_id": 1, "x_pos": 0, "y_pos": 0},
            {"plant_id": 10, "room_id": 1, "x_pos": 0, "y_pos": 0},
            {"plant_id": 11, "room_id": 1, "x_pos": 0, "y_pos": 0},
            {"plant_id": 12, "room_id": 1, "x_pos": 0, "y_pos": 0},
            {"plant_id": 13, "room_id": 1, "x_pos": 0, "y_pos": 0},
            {"plant_id": 14, "room_id": 1, "x_pos": 0, "y_pos": 0},
            {"plant_id": 15, "room_id": 1, "x_pos": 0, "y_pos": 0},
            {"plant_id": 16, "room_id": 1, "x_pos": 0, "y_pos": 0},
            {"plant_id": 17, "room_id": 1, "x_pos": 0, "y_pos": 0},
        ]
    )


def downgrade() -> None:
    pass
