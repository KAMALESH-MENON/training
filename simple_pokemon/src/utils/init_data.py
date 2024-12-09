import requests

class LoadData:

    @classmethod
    def add_data(cls):
        pokemon_url = "https://raw.githubusercontent.com/DetainedDeveloper/Pokedex/master/pokedex_raw/pokedex_raw_array.json"
        response = requests.get(url=pokemon_url, timeout=10)

        if response.status_code == 200:
            pokemons = response.json()
            pokemon_dict = {
                pokemon["id"]: pokemon for pokemon in pokemons
                }
            return pokemon_dict
        else:
            response.raise_for_status()

if __name__ == "__main__":
    data = LoadData.add_data()
    print(data.get(1))
