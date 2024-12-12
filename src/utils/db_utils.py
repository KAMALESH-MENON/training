from src.config.database import connection


def create_tables():
    with connection.cursor() as cursor:
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS public.pokemon (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                height INT,
                weight INT,
                xp INT,
                image_url VARCHAR(255),
                pokemon_url VARCHAR(255)
            );
        """
        )
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS public.abilities (
                id SERIAL PRIMARY KEY,
                pokemon_id INT REFERENCES public.pokemon(id) ON DELETE CASCADE,
                ability_name VARCHAR(100),
                is_hidden BOOLEAN
            );
        """
        )
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS public.stats (
                id SERIAL PRIMARY KEY,
                pokemon_id INT REFERENCES public.pokemon(id) ON DELETE CASCADE,
                stat_name VARCHAR(100),
                stat_value INT
            );
        """
        )
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS public.types (
                id SERIAL PRIMARY KEY,
                pokemon_id INT REFERENCES public.pokemon(id) ON DELETE CASCADE,
                type_name VARCHAR(100)
            );
        """
        )
        connection.commit()


def insert_pokemon(pokemon_data):
    with connection.cursor() as cursor:
        for pokemon in pokemon_data.values():
            cursor.execute(
                """ 
                SELECT 
                    1 
                FROM 
                    public.pokemon WHERE id = %s; """,
                (pokemon["id"],),
            )
            pokemon_exists = cursor.fetchone()
            if not pokemon_exists:
                cursor.execute(
                    """
                    INSERT INTO public.pokemon (id, name, height, weight, xp, image_url, pokemon_url)
                    VALUES (%s, %s, %s, %s, %s, %s, %s);
                """,
                    (
                        pokemon["id"],
                        pokemon["name"],
                        pokemon["height"],
                        pokemon["weight"],
                        pokemon["xp"],
                        pokemon["image_url"],
                        pokemon["pokemon_url"],
                    ),
                )

                for ability in pokemon["abilities"]:
                    cursor.execute(
                        """
                        INSERT INTO public.abilities (pokemon_id, ability_name, is_hidden)
                        VALUES (%s, %s, %s);
                    """,
                        (pokemon["id"], ability["name"], ability["is_hidden"]),
                    )

                for stat in pokemon["stats"]:
                    cursor.execute(
                        """
                        INSERT INTO public.stats (pokemon_id, stat_name, stat_value)
                        VALUES (%s, %s, %s);
                    """,
                        (pokemon["id"], stat["name"], stat["base_stat"]),
                    )

                for ptype in pokemon["types"]:
                    cursor.execute(
                        """
                        INSERT INTO public.types (pokemon_id, type_name)
                        VALUES (%s, %s);
                    """,
                        (pokemon["id"], ptype["name"]),
                    )
            connection.commit()
        cursor.execute(
            """
                SELECT setval('public.pokemon_id_seq', (SELECT MAX(id) FROM public.pokemon));
            """
        )
