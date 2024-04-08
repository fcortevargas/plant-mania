from fastapi import FastAPI

from app.domains.plants.router import plant_router
from app.domains.species.router import species_router
from app.domains.users.router import user_router

app = FastAPI()

app.include_router(user_router)
app.include_router(plant_router)
app.include_router(species_router)


@app.get("/")
def main():
    return {"Hello": "World"}
