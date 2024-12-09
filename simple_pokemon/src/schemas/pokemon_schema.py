from pydantic import BaseModel, HttpUrl
from typing import List, Optional

class Ability(BaseModel):
    name: str
    is_hidden: bool

class Stat(BaseModel):
    name: str
    base_stat: int

class Type(BaseModel):
    name: str

class PokemonBase(BaseModel):
    name: str
    height: int
    weight: int
    xp: int
    image_url: HttpUrl
    pokemon_url: HttpUrl
    abilities: List[Ability]
    stats: List[Stat]
    types: List[Type]

class PokemonInput(PokemonBase):
    pass

class PokemonOutput(PokemonBase):
    id: int

class PokemonUpdate(BaseModel):
    name: Optional[str] = None
    height: Optional[int] = None
    weight: Optional[int] = None
    xp: Optional[int] = None
    image_url: Optional[HttpUrl] = None
    pokemon_url: Optional[HttpUrl] = None
    abilities: Optional[List[Ability]] = None
    stats: Optional[List[Stat]] = None
    types: Optional[List[Type]] = None
