from fastapi import FastAPI

from app.domains.users.router import user_router

app = FastAPI()

app.include_router(user_router)


@app.get("/")
def main():
    return {"Hello": "World"}