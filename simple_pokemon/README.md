# Simple Pokemon API

## Overview
You can list, search, create, update, and delete Pokemon records. The API is built using FastAPI and includes features such as pagination, query-based search, and schema validation.

---

## Features

### 1. **List All Pokemon**
Retrieve a paginated list of Pokemon.

- **Endpoint**: `GET /pokemon`
- **Query Parameters**:
  - `page` (default: 1) - The page number to retrieve (must be greater than 0).
  - `size` (default: 10) - The number of records per page (between 5 and 100).
- **Responses**:
  - `200 OK`: Returns the Pokemon list for the specified page.
  - `400 Bad Request`: If the page number exceeds the maximum.
  - `404 Not Found`: If no Pokemon are found.

---

### 2. **Retrieve a Pokemon by ID**
Fetch the details of a Pokemon by its ID.

- **Endpoint**: `GET /pokemon/{id}`
- **Path Parameter**:
  - `id` - The ID of the Pokemon.
- **Responses**:
  - `200 OK`: Returns the Pokemon details.
  - `404 Not Found`: If no Pokemon with the given ID exists.

---

### 3. **Search Pokemon by Name**
Search for Pokemon by their name.

- **Endpoint**: `GET /pokemon/search/name`
- **Query Parameter**:
  - `name` - The name of the Pokemon to search.
- **Responses**:
  - `200 OK`: Returns a list of matching Pokemon.
  - `404 Not Found`: If no Pokemon with the given name exists.

---

### 4. **Search Pokemon by Type**
Search for Pokemon based on their type(s).

- **Endpoint**: `GET /pokemon/search/type`
- **Query Parameter**:
  - `type` - A list of types to search for (e.g., `?type=fire&type=water`).
- **Responses**:
  - `200 OK`: Returns a list of matching Pokemon.
  - `400 Bad Request`: If the type parameter is missing.
  - `404 Not Found`: If no Pokemon with the given type(s) are found.

---

### 5. **Create a New Pokemon**
Add a new Pokemon to the dataset.

- **Endpoint**: `POST /pokemon/{id}`
- **Body**:
  - JSON representation of the Pokemon.
- **Responses**:
  - `201 Created`: Returns the newly added Pokemon.

---

### 6. **Update an Existing Pokemon**
Partially update an existing Pokemon.

- **Endpoint**: `PATCH /pokemon/{id}`
- **Path Parameter**:
  - `id` - The ID of the Pokemon to update.
- **Body**:
  - JSON with fields to update.
- **Responses**:
  - `200 OK`: Returns the updated Pokemon.
  - `404 Not Found`: If no Pokemon with the given ID exists.

---

### 7. **Delete a Pokemon**
Remove a Pokemon from the dataset.

- **Endpoint**: `DELETE /pokemon/{id}`
- **Path Parameter**:
  - `id` - The ID of the Pokemon to delete.
- **Responses**:
  - `200 OK`: If the Pokemon is successfully deleted.
  - `404 Not Found`: If no Pokemon with the given ID exists.

---