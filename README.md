# Pokedex API

This project is a FastAPI-based application that follows Repository Pattern and Service Layer for managing a Pokedex. It provides CRUD operations for Pokemon data and allows search adnd filtering Pokemon with various parameters.

## Project Structure

Top-level directory layout
```
.
├── src
├── requirements.txt
└── README.md
```
Source files follows repository pattern and service layer.
```
.
├── ...
├── src           
│   ├── config 
│   │   └── database.py
│   ├── repository
│   │   └── crud_repository.py
│   ├── router
│   │   └── crud.py
│   ├── schemas
│   │   └── pokemon_schema.py
│   ├── service 
│   │   └── crud_service.py
│   ├── utils
│   │   ├── db_utils.py
│   │   └── init_data.py
│   └── main.py
└── ...

```
### Key Components

- **`database.py`**: Config file for connecting to Postgres database.
- **`crud_repository.py`**: The repository layer consists of classes responsible for database operations.
- **`crud.py`**: Defines API routes for creating, reading, updating, deleting, and listing Pokemon.
- **`shared_data.py`**: Contains the shared data storage (`pokemons` dictionary) for Pokemon records.
- **`pokemon_schemas.py`**: Contains Pydantic models for Pokemon input, output, and updates.
- **`crud_service.py`**: The service layer acts as the intermediary between the API endpoints and the repository layer. 
- **`db_utils.py`**: Functions to create and populate a PostgreSQL database with tables
- **`init_data.py`**: Fetches and loads initial Pokemon data from a remote JSON file.
- **`main.py`**: Initializes the FastAPI application and integrates the routes and shared data.

## Features

  ## 1. Data Initialization

  -  Populates pokemon data from a remote JSON source when the application starts after creation of tables in database.

  ## 2. CRUD Operations

  - **Create Pokemon**: Adds a new Pokemon to the database.
  - **Read Pokemon**: Fetches details of a specific Pokemon by its ID.
  - **List Pokemons**: Fetches details of a pokemons with or without serach and filter conditions.
    - Paginated listing of Pokemon.
    - Search by 
      - name
      - height
      - weight
      - xp
    - Filters by 
      - mininum height & maximum height
      - mininum weight & maximum weight
      - mininum xp & maximum xp
  - **Update Pokemon**: Updates details of a specific Pokemon.
  - **Delete Pokemon**: Removes a Pokemon from the database.

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
| `GET`    | `/pokemon`              | Lists, search and filters Pokemon.|
| `GET`    | `/pokemon/{pokemon_id}` | Get details of a specific Pokemon.|
| `PUT`    | `/pokemon/{pokemon_id}` | Update a Pokemon.                |
| `DELETE` | `/pokemon/{pokemon_id}` | Delete a Pokemon.                |


## External Data Source

The application fetches Pokemon data from:
- [https://raw.githubusercontent.com/DetainedDeveloper/Pokedex/master/pokedex_raw/pokedex_raw_array.json](https://raw.githubusercontent.com/DetainedDeveloper/Pokedex/master/pokedex_raw/pokedex_raw_array.json)
