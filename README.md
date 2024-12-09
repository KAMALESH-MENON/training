# Pokedex API

This project is a FastAPI-based application for managing a Pokedex. It provides CRUD operations for Pokemon data and allows filtering and listing Pokemon with various parameters.

## Project Structure

```
src/
├── data/
│   └── shared_data.py
├── main.py
├── router/
│   └── crud.py
├── schemas/
│   └── pokemon_schemas.py
└── util/
    └── init_data.py
```

### Key Components

- **`shared_data.py`**: Contains the shared data storage (`pokemons` dictionary) for Pokemon records.
- **`crud.py`**: Defines API routes for creating, reading, updating, deleting, and listing Pokemon.
- **`pokemon_schemas.py`**: Contains Pydantic models for Pokemon input, output, and updates.
- **`init_data.py`**: Fetches and loads initial Pokemon data from a remote JSON file.
- **`main.py`**: Initializes the FastAPI application and integrates the routes and shared data.

## Features

### CRUD Operations

- **Create Pokemon**: Adds a new Pokemon to the database.
- **Read Pokemon**: Fetches details of a specific Pokemon by its ID.
- **Update Pokemon**: Updates details of a specific Pokemon.
- **Partially Update Pokemon**: Updates specific fields of a Pokemon.
- **Delete Pokemon**: Removes a Pokemon from the database.

### Listing and Filtering

- Paginated listing of Pokemon.
- Filters by name, height, weight, and experience points (XP).

### Data Initialization

- Loads initial Pokemon data from a remote JSON source when the application starts.

## Installation

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   uvicorn src.main:app --reload
   ```

3. Open the documentation in your browser:
   - **Swagger UI**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## API Endpoints

### Base URL
`http://127.0.0.1:8000`

### Endpoints

| Method   | Endpoint                | Description                       |
|----------|-------------------------|-----------------------------------|
| `POST`   | `/pokemon`              | Create a new Pokemon.            |
| `GET`    | `/pokemon/{pokemon_id}` | Get details of a specific Pokemon.|
| `PUT`    | `/pokemon/{pokemon_id}` | Update a Pokemon.                |
| `PATCH`  | `/pokemon/{pokemon_id}` | Partially update a Pokemon.      |
| `DELETE` | `/pokemon/{pokemon_id}` | Delete a Pokemon.                |
| `GET`    | `/pokemon`              | List and filter Pokemon.         |


## External Data Source

The application fetches Pokemon data from:
- [https://raw.githubusercontent.com/DetainedDeveloper/Pokedex/master/pokedex_raw/pokedex_raw_array.json](https://raw.githubusercontent.com/DetainedDeveloper/Pokedex/master/pokedex_raw/pokedex_raw_array.json)
