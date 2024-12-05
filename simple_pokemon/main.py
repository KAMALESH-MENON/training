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

@app.get("/pokemon", tags=["Pokedex"], response_model=List[Pokemon])
async def list_pokemon(
    page: int = Query(1, gt=0),
    size: int = Query(10, ge=5, le=100),
    name: Optional[str] = Query(None, description="Search by Pokemon name"),
    min_height: Optional[int] = Query(None, description="Filter by minimum height", gt=0),
    max_height: Optional[int] = Query(None, description="Filter by maximum height", gt=0),
    min_weight: Optional[int] = Query(None, description="Filter by minimum weight", gt=0),
    max_weight: Optional[int] = Query(None, description="Filter by maximum weight", gt=0),
    min_xp: Optional[int] = Query(None, description="Filter by minimum XP", gt=0),
    max_xp: Optional[int] = Query(None, description="Filter by maximum XP", gt=0),
    ability: Optional[str] = Query(None, description="Filter by ability name"),
    ):

    search_results = pokemons

    #search
    if name is not None:
        search_results = [
            pokemon for pokemon in search_results
            if name.lower() in pokemon['name'].lower()
            ]

    #filter
    if min_height is not None:
        search_results = [pokemon for pokemon in search_results if pokemon['height'] >= min_height]
    if max_height is not None:
        search_results = [pokemon for pokemon in search_results if pokemon['height'] <= max_height]
    if min_weight is not None:
        search_results = [pokemon for pokemon in search_results if pokemon['weight'] >= min_weight]
    if max_weight is not None:
        search_results = [pokemon for pokemon in search_results if pokemon['weight'] <= max_weight]
    if min_xp is not None:
        search_results = [pokemon for pokemon in search_results if pokemon['xp'] >= min_xp]
    if max_xp is not None:
        search_results = [pokemon for pokemon in search_results if pokemon['xp'] <= max_xp]
    if ability is not None:
        search_results = [
            pokemon for pokemon in search_results 
            if any(a['name'].lower() == ability.lower() for a in pokemon['abilities'])
            ]

    page_end = (len(search_results) + size - 1) // size

    if page > page_end:
        page = page_end


    start = (page-1) * size
    end = start + size

    if search_results:
        return search_results[start:end]
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
    if not pokemons:
        new_pokemon.id = 1
    else:
        max_id = max(pokemon["id"] for pokemon in pokemons)
        new_pokemon.id = max_id + 1
    pokemons.append(new_pokemon.model_dump())
    return {"detail": "Added pokemon.", "pokemon": new_pokemon}


@app.put("/pokemon/{id}", tags=["Pokedex"], response_model=Pokemon)
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
