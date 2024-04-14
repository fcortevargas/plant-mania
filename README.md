# Plant Mania

This is the repository of a plant management app designed to automate and enhance the care of home plants.

## Cloning

Clone the project

```bash
  git clone https://github.com/fcortevargas/plant-mania.git
```

Go to the project directory

```bash
  cd plant-mania
```

## Containerization

The database and the backend are containerized using Docker to simplify the development and to ensure that the
application runs consistently across different environments.

To run the Docker containers for the database and the backend:

```bash
  docker-compose up
```

## Database Migrations

This project uses Alembic to handle database migrations. To create a migration:

```bash
  alembic revision -m "description"
```

Then, to upgrade to the latest revision:

```bash
  alembic -n <name> upgrade head
```

To downgrade all the way to the first revision:

```bash
  alembic --n <name> downgrade base
```

## API Reference

To see the documentation of the FastAPI endpoints:

```http
  http://localhost:8000/docs
```

## ER Diagram

![ER Diagram](https://github.com/fcortevargas/plant-mania/blob/main/ER.png)
