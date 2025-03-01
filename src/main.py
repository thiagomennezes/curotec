from .dao import dao
from .router import api_router
from fastapi import FastAPI


def create_app() -> FastAPI:
    app = FastAPI(title="CurotecChallenge")
    app.include_router(api_router)
    return app

app = create_app()
dao.create_tables()