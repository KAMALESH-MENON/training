from src.config.database import connection
from src.schemas.pokemon_schema import PokemonInput, PokemonUpdate, PokemonOutput
from typing import List

class CrudRepository:
    def __init__(self):
        pass

    def list_pokemons_repository(
        self, name,
        min_height, max_height,
        min_weight, max_weight,
        min_xp, max_xp,
        page, size
        ) -> List[PokemonOutput]:
        offset = (page - 1) * size
        
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT 
                    p.id,
                    p.name,
                    p.height,
                    p.weight,
                    p.xp,
                    p.image_url,
                    p.pokemon_url,
                    JSON_AGG(DISTINCT jsonb_build_object('name', a.ability_name, 'is_hidden', a.is_hidden)) AS abilities,
                    JSON_AGG(DISTINCT jsonb_build_object('name', s.stat_name, 'base_stat', s.stat_value)) AS stats,
                    JSON_AGG(DISTINCT jsonb_build_object('name', t.type_name)) AS types
                FROM 
                    public.pokemon p 
                INNER JOIN 
                    public.abilities a ON p.id = a.pokemon_id 
                INNER JOIN 
                    public.stats s ON p.id = s.pokemon_id
                INNER JOIN 
                    public.types t ON p.id = t.pokemon_id 
                GROUP BY
                    p.id
                ;
                """,
                (size, offset,)
            )
            rows = cursor.fetchall()
            pokemons = [self.convert_tuple_to_pokemon_object(row) for row in rows]
            return pokemons


    def read_pokemon_repository(self, pokemon_id: int) -> PokemonOutput:
        with connection.cursor() as cursor:
            cursor.execute(
                """ 
                SELECT 
                    p.id,
                    p.name,
                    p.height,
                    p.weight,
                    p.xp,
                    p.image_url,
                    p.pokemon_url,
                    (
                        SELECT JSONB_AGG(jsonb_build_object('name', a.ability_name, 'is_hidden', a.is_hidden))
                        FROM public.abilities a
                        WHERE p.id = a.pokemon_id
                    ) AS abilities,
                    (
                        SELECT JSONB_AGG(jsonb_build_object('name', s.stat_name, 'base_stat', s.stat_value))
                        FROM public.stats s
                        WHERE p.id = s.pokemon_id
                    ) AS stats,
                    (
                        SELECT JSONB_AGG(jsonb_build_object('name', t.type_name))
                        FROM public.types t
                        WHERE p.id = t.pokemon_id
                    ) AS types
                FROM 
                    public.pokemon p 
                WHERE
                    p.id = %s
                ;
                """,
                (pokemon_id,)
            )
            row = cursor.fetchone()
            if row is None:
                return None
            pokemon = self.convert_tuple_to_pokemon_object(row)

            return pokemon


    def create_pokemon_repository(self, pokemon: PokemonInput) -> PokemonOutput:
        pokemon = pokemon.model_dump(exclude_none=True)
        with connection.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO 
                    public.pokemon (name, height, weight, xp, image_url, pokemon_url)
                VALUES 
                    (%s, %s, %s, %s, %s, %s)
                RETURNING id
                ;
                """,
                (
                    pokemon.get("name"),
                    pokemon.get("height"),
                    pokemon.get("weight"),
                    pokemon.get("xp"),
                    str(pokemon.get("image_url")),
                    str(pokemon.get("pokemon_url")),
                ),
            )
            pokemon_id = cursor.fetchone()[0]

            for ability in pokemon.get("abilities", []):
                cursor.execute(
                    """
                    INSERT INTO 
                        public.abilities (pokemon_id, ability_name, is_hidden)
                    VALUES 
                        (%s, %s, %s)
                    ;
                    """,
                        (pokemon_id, ability["name"], ability["is_hidden"]),
                )

            for stat in pokemon.get("stats", []):
                cursor.execute(
                    """
                    INSERT INTO 
                        public.stats (pokemon_id, stat_name, stat_value)
                    VALUES 
                        (%s, %s, %s)
                    ;
                    """,
                        (pokemon_id, stat["name"], stat["base_stat"]),
                )

            for type in pokemon.get("types", []):
                cursor.execute(
                    """
                    INSERT INTO public.types (pokemon_id, type_name)
                    VALUES (%s, %s)
                    ;
                    """,
                        (pokemon_id, type["name"]),
                )
            connection.commit()

            pokemon = self.read_pokemon_repository(pokemon_id)
            return pokemon


    def update_pokemon_repository(self, pokemon_id: int, pokemon: PokemonUpdate) -> PokemonUpdate:
        pokemon = pokemon.model_dump()
        with connection.cursor() as cursor:
            cursor.execute(
                """
                UPDATE 
                    public.pokemon
                SET 
                    name = %s, 
                    height = %s, 
                    weight = %s, 
                    xp = %s, 
                    image_url = %s, 
                    pokemon_url = %s
                WHERE 
                    id = %s;
                """,
                    (
                    pokemon.get("name"),
                    pokemon.get("height"),
                    pokemon.get("weight"),
                    pokemon.get("xp"),
                    str(pokemon.get("image_url")),
                    str(pokemon.get("pokemon_url")),
                    pokemon_id,
                    ),
            )

            cursor.execute(
                """
                DELETE FROM 
                    public.abilities 
                WHERE 
                    pokemon_id = %s;
                """,
                    (pokemon_id,)
            )
            for ability in pokemon.get("abilities", []):
                cursor.execute(
                    """
                    INSERT INTO 
                        public.abilities (pokemon_id, ability_name, is_hidden)
                    VALUES 
                        (%s, %s, %s)
                    ;
                    """,
                        (pokemon_id, ability["name"], ability["is_hidden"]),
                )

            cursor.execute(
                """
                DELETE FROM 
                    public.stats 
                WHERE 
                    pokemon_id = %s
                ;
                """,
                    (pokemon_id,)
            )
            for stat in pokemon.get("stats", []):
                cursor.execute(
                    """
                    INSERT INTO 
                        public.stats (pokemon_id, stat_name, stat_value)
                    VALUES 
                        (%s, %s, %s)
                    ;
                    """,
                        (pokemon_id, stat["name"], stat["base_stat"]),
                )

            cursor.execute(
                """
                DELETE FROM 
                    public.types 
                WHERE
                    pokemon_id = %s
                ;""",
                    (pokemon_id,)
            )
            for type in pokemon.get("types", []):
                cursor.execute(
                    """
                    INSERT INTO 
                        public.types (pokemon_id, type_name)
                    VALUES 
                        (%s, %s)
                    ;
                    """,
                        (pokemon_id, type["name"]),
                )
            connection.commit()

            updated_pokemon = self.read_pokemon_repository(pokemon_id)
            return updated_pokemon


    def delete_pokemon_repository(self, pokemon_id: int) -> bool:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                DELETE FROM 
                    public.pokemon 
                WHERE 
                    id = %s
                ;
                """,
                    (pokemon_id,)
                )
            connection.commit()
            return True


    def pokemon_exists_by_name(self, name: str) -> bool:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT 
                    1 
                FROM 
                    public.pokemon 
                WHERE 
                    name = %s
                ;
                """,
                    (name,)
                )


    @staticmethod
    def convert_tuple_to_pokemon_object(row: tuple) -> PokemonOutput:
        return PokemonOutput(
            id=row[0],
            name=row[1],
            height=row[2],
            weight=row[3],
            xp=row[4],
            image_url=row[5],
            pokemon_url=row[6],
            abilities=row[7],
            stats=row[8],
            types=row[9]
            )