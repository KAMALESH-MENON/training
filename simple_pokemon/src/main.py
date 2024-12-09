from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.router import crud
from src.utils.init_data import LoadData
from src.data.shared_data import pokemons


@asynccontextmanager
async def load_data(app: FastAPI):
    """
    Initializes the pokemons data when the application starts up.
    """
    pokemons.update(LoadData.add_data())
    yield


app = FastAPI(
    docs_url="/",
    lifespan=load_data
    )

app.include_router(crud.router)
