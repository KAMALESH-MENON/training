from pydantic import BaseModel, HttpUrl, Field
from typing import List

class Ability(BaseModel):
    name: str
    is_hidden: bool

class Stat(BaseModel):
    name: str
    base_stat: int

class Type(BaseModel):
    name: str

class Pokemon(BaseModel):
    id: int
    name: str = None
    height: int = None
    weight: int  = None
    xp: int = None
    image_url: HttpUrl = None
    pokemon_url: HttpUrl = None
    abilities: List[Ability] = None
    stats: List[Stat] = None
    types: List[Type] = None

class UpdatePokemon(BaseModel):
    name: str = None
    height: int = None
    weight: int  = None
    xp: int = None
    image_url: HttpUrl = None
    pokemon_url: HttpUrl = None
    abilities: List[Ability] = None
    stats: List[Stat] = None
    types: List[Type] = None
