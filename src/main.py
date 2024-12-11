from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.router import crud
from src.utils.init_data import LoadData


@asynccontextmanager
async def load_data(app: FastAPI):
    """
    Initializes the pokemons data when the application starts up.
    """
    LoadData.add_data()
    yield


app = FastAPI(
    lifespan=load_data
    )

app.include_router(crud.router)
