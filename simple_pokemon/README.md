# Simple Pokemon API

## Features

### 1. **List All Pokemon**

Retrieve a paginated list of Pokemon.

- **Endpoint**: `GET /pokemon`
- **Query Parameters**:
  - `page` (default: 1): Page number (must be > 0).
  - `size` (default: 10): Number of results per page (between 5 and 100).
  - Search:
    - `name`: Search by name (e.g., bulbasaur).
  - **Filters**:
    - `min_height`, `max_height`: Filter by height range.
    - `min_weight`, `max_weight`: Filter by weight range.
    - `min_xp`, `max_xp`: Filter by experience points.
    - `ability`: Filter by ability name.
- **Responses**:
  - `200 OK`: Paginated results of Pokemon.
  - `404 Not Found`: No Pokemon found.

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

### 3. **Create a New Pokemon**
Add a new Pokemon to the dataset.

- **Endpoint**: `POST /pokemon/{id}`
- **Body**:
  - JSON representation of the Pokemon.
- **Responses**:
  - `201 Created`: Returns the newly added Pokemon.


---

### 4. **Update an Existing Pokemon**
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

### 5. **Delete a Pokemon**

Remove a Pokemon from the dataset.

- **Endpoint**: `DELETE /pokemon/{id}`
- **Path Parameter**:
  - `id` - The ID of the Pokemon to delete.
- **Responses**:
  - `200 OK`: If the Pokemon is successfully deleted.
  - `404 Not Found`: If no Pokemon with the given ID exists.
---
