from pydantic import BaseModel, HttpUrl
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
    name: str | None = None
    height: int | None = None
    weight: int  | None = None
    xp: int | None = None
    image_url: HttpUrl | None = None
    pokemon_url: HttpUrl | None = None
    abilities: List[Ability]
    stats: List[Stat]
    types: List[Type]
