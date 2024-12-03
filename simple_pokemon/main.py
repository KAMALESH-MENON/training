import json
from typing import List, Optional
from fastapi import FastAPI, HTTPException, status, Query
from simple_pokemon.schemas import Pokemon, UpdatePokemon

app = FastAPI(
    docs_url="/",
    title="Simple Pokemon",
    )

pokemons = []

file_path = "simple_pokemon/pokedex_raw_array.json"

def load_data():
    with open(file_path, "r") as file:
        pokemons.extend(json.load(file))
    return f'total {len(pokemons)} pokemon added.'

load_data()

@app.get("/pokemon", tags=["Pokedex"])
async def list_pokemon(page: int = Query(1, gt=0), size: int = Query(10, ge=5, le=100)):
    page_end = (len(pokemons) + size - 1) // size
    if page > page_end:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Page exceeds max page number."
        )

    start = (page-1) * size
    end = start + size

    if pokemons:
        return pokemons[start:end]
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="No pokemon found."
        )


@app.get("/pokemon/{id}", tags=["Pokedex"], response_model=Pokemon)
async def retrieve_pokemon(id: int):
    for pokemon in pokemons:
        if pokemon["id"] == id:
            return pokemon
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"No pokemon with id: {id}"
        )


@app.post("/pokemon/{id}", tags=["Pokedex"], status_code=status.HTTP_201_CREATED)
async def create_pokemon(new_pokemon: Pokemon):
    new_pokemon.id = len(pokemons) + 1
    pokemons.append(new_pokemon.model_dump())
    return {"detail": "Added pokemon.", "pokemon": new_pokemon}


@app.patch("/pokemon/{id}", tags=["Pokedex"], response_model=Pokemon)
async def partial_update(id: int, updated_data: UpdatePokemon):
    for pokemon in pokemons:
        if pokemon["id"] == id:
            for key, value in updated_data.model_dump().items():
                if value is not None:
                    pokemon[key] = value
            return pokemon

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Pokemon with id {id} not found."
        )


@app.delete("/pokemon/{id}", tags=["Pokedex"], status_code=status.HTTP_200_OK)
async def delete_pokemon(id: int):
    for index, pokemon in enumerate(pokemons):
        if pokemon["id"] == id:
            pokemons.pop(index)
            return {
                "detail": f"Pokemon with id = {id}, has been deleted."
            }
    raise HTTPException(
        detail=f"Pokemon with id: {id} not found.",
        status_code= status.HTTP_404_NOT_FOUND
    )
