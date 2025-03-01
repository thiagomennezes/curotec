from .dao import dao
from .router import api_router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

def create_app() -> FastAPI:
    app = FastAPI(title="CurotecChallenge")
    app.add_middleware(
        CORSMiddleware,
        allow_origins = ["*"],
        allow_credentials = True,
        allow_methods = ["*"],
        allow_headers = ["*"],
)       
    app.include_router(api_router)
    return app

app = create_app()
dao.create_tables()