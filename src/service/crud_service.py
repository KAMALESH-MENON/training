from fastapi import HTTPException, Query
from src.repository.crud_repository import CrudRepository
from src.schemas.pokemon_schema import PokemonOutput, PokemonInput, PokemonUpdate

class CrudService:
    def __init__(self):
        self.repository = CrudRepository()

    def list_pokemons_service(
        self,
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
        rows = self.repository.list_pokemons_repository(
            page=page, size=size, name=name,
            min_height=min_height, max_height=max_height,
            min_weight=min_weight, max_weight=max_weight,
            min_xp=min_xp, max_xp=max_xp
        )
      
        return rows

    def read_pokemon_service(self, pokemon_id: int) -> PokemonOutput:
        pokemon = self.repository.read_pokemon_repository(pokemon_id)
        if pokemon is None:
            raise HTTPException(status_code=404, detail="Pokemon not found")
        return pokemon

    def create_pokemon_service(self, pokemon: PokemonInput) -> PokemonOutput:
        if self.repository.pokemon_exists_by_name(pokemon.name):
            raise HTTPException(status_code=400, detail="Pokemon already exists")
        return self.repository.create_pokemon_repository(pokemon)

    def update_pokemon_service(self, pokemon_id: int, pokemon: PokemonUpdate) -> PokemonOutput:
        if not self.repository.read_pokemon_repository(pokemon_id):
            raise HTTPException(status_code=404, detail="Pokemon not found")
        return self.repository.update_pokemon_repository(pokemon_id, pokemon)

    def delete_pokemon_service(self, pokemon_id: int) -> bool:
        if not self.repository.read_pokemon_repository(pokemon_id):
            raise HTTPException(status_code=404, detail="Pokemon not found")
        self.repository.delete_pokemon_repository(pokemon_id)
        return True
