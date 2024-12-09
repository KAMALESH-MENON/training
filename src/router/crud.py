from typing import List
from fastapi import APIRouter, HTTPException, Query, status
from src.schemas.pokemon_schema import PokemonInput, PokemonUpdate
from src.data.shared_data import pokemons

router = APIRouter(
    prefix="/pokemon",
    tags=["Pokedex"]
)

@router.post("", status_code=status.HTTP_201_CREATED)
async def create_pokemon(data: PokemonInput):
    pokemon_id = max(pokemons.keys()) + 1 if pokemons else 1
    pokemon = {"id":pokemon_id}
    pokemon.update(data.model_dump())
    pokemons[pokemon_id] = pokemon
    return {
        "detail": "The pokemon was created successfully.",
        "pokemon": pokemon
        }

@router.get("/{pokemon_id}")
async def read_pokemon(pokemon_id: int):
    if pokemon_id not in pokemons:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pokemon not found.")
    return pokemons[pokemon_id]

@router.put("/{pokemon_id}", status_code= status.HTTP_200_OK)
async def update_pokemon(pokemon_id: int, data: PokemonUpdate):
    if pokemon_id not in pokemons:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pokemon not found.")
    pokemons[pokemon_id] = data.model_dump()
    return {
        "detail": "The pokemon was Updated successfully.",
        "data": pokemons[pokemon_id]
        }
    
@router.patch("/{pokemon_id}", status_code= status.HTTP_200_OK)
async def partial_update_pokemon(pokemon_id: int, data: PokemonUpdate):
    if pokemon_id not in pokemons:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pokemon not found.")
    pokemon = pokemons[pokemon_id]
    update_data = data.model_dump()
    for key, value in update_data.items():
        if value is not None:
            pokemon[key] = value
    return {
        "detail": "The pokemon was Updated successfully.",
        "data": pokemon
    }

@router.delete("/{pokemon_id}", status_code= status.HTTP_200_OK)
async def delete_pokemon(pokemon_id: int):
    if pokemon_id not in pokemons:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pokemon not found.")
    del pokemons[pokemon_id]
    return {"detail": "The pokemon was deleted successfully."}

@router.get("")
async def list_pokemons(
    page: int = Query(1, gt=0),
    size: int = Query(10, gt=0, le=100),
    name: str = Query(None, description="Search by Pokemon name"),
    min_height: int = Query(None, description="Filter by minimum height", gt=0),
    max_height: int = Query(None, description="Filter by maximum height", gt=0),
    min_weight: int = Query(None, description="Filter by minimum weight", gt=0),
    max_weight: int = Query(None, description="Filter by maximum weight", gt=0),
    min_xp: int = Query(None, description="Filter by minimum XP", gt=0),
    max_xp: int = Query(None, description="Filter by maximum XP", gt=0)
    ):

    if min_height and max_height and min_height > max_height:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="mininum height cannot be greater than maximum height"
            )
    if min_weight and max_weight and min_weight > max_weight:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="mininum weight cannot be greater than maximum weight"
            )
    if min_xp and max_xp and min_xp > max_xp:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="mininum xp cannot be greater than maximum xp"
            )

    search_results = list(pokemons.values())

    if name:
        search_results = list(
            filter(lambda pokemon: name.lower() in pokemon["name"].lower(), search_results)
            )
    if min_height:
        search_results = list(
            filter(lambda pokemon: pokemon["height"] >= min_height, search_results)
            )
    if max_height:
        search_results = list(
            filter(lambda pokemon: pokemon["height"] <= max_height, search_results)
            )
    if min_weight:
        search_results = list(
            filter(lambda pokemon: pokemon["weight"] >= min_weight, search_results)
            )
    if max_weight:
        search_results = list(
            filter(lambda pokemon: pokemon["weight"] <= max_weight, search_results)
            )
    if min_xp:
        search_results = list(
            filter(lambda pokemon: pokemon["xp"] >= min_xp, search_results)
            )
    if max_xp:
        search_results = list(
            filter(lambda pokemon: pokemon["xp"] <= max_xp, search_results)
            )

    start = (page - 1) * size
    end = start + size
    return search_results[start:end]
