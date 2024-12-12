from typing import List
from fastapi import APIRouter, Query, HTTPException, status
from src.schemas.pokemon_schema import PokemonInput, PokemonOutput, PokemonUpdate
from src.service.crud_service import CrudService as service

router = APIRouter(prefix="/pokemon", tags=["Pokedex"])


@router.post("", status_code=status.HTTP_201_CREATED, response_model=PokemonOutput)
async def create_pokemon(pokemon: PokemonInput):
    _service = service()
    return _service.create_pokemon_service(pokemon)


@router.get(
    "/{pokemon_id}", status_code=status.HTTP_200_OK, response_model=PokemonOutput
)
def read_pokemon(pokemon_id: int):
    _service = service()
    return _service.read_pokemon_service(pokemon_id=pokemon_id)


@router.put(
    "/{pokemon_id}", status_code=status.HTTP_200_OK, response_model=PokemonOutput
)
def update_pokemon(pokemon_id: int, pokemon: PokemonUpdate):
    _service = service()
    return _service.update_pokemon_service(pokemon_id, pokemon)


@router.delete("/{pokemon_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_pokemon(pokemon_id: int):
    _service = service()
    return _service.delete_pokemon_service(pokemon_id)


@router.get("", status_code=status.HTTP_200_OK, response_model=List[PokemonOutput])
def list_pokemons(
    page: int = Query(1, gt=0),
    size: int = Query(10, gt=0, le=100),
    name: str = Query(None, description="Search by Pokemon name"),
    height: int = Query(None, description="Search by Pokemon height"),
    weight: int = Query(None, description="Search by Pokemon weight"),
    xp: int = Query(None, description="Search by Pokemon xp"),
    min_height: int = Query(None, description="Filter by minimum height", gt=0),
    max_height: int = Query(None, description="Filter by maximum height", gt=0),
    min_weight: int = Query(None, description="Filter by minimum weight", gt=0),
    max_weight: int = Query(None, description="Filter by maximum weight", gt=0),
    min_xp: int = Query(None, description="Filter by minimum XP", gt=0),
    max_xp: int = Query(None, description="Filter by maximum XP", gt=0),
):
    if min_height and max_height and min_height > max_height:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Minimum height cannot be greater than maximum height",
        )
    if min_weight and max_weight and min_weight > max_weight:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Minimum weight cannot be greater than maximum weight",
        )
    if min_xp and max_xp and min_xp > max_xp:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Minimum XP cannot be greater than maximum XP",
        )

    _service = service()
    return _service.list_pokemons_service(
        page=page,
        size=size,
        name=name,
        height=height,
        weight=weight,
        xp=xp,
        min_height=min_height,
        max_height=max_height,
        min_weight=min_weight,
        max_weight=max_weight,
        min_xp=min_xp,
        max_xp=max_xp,
    )
