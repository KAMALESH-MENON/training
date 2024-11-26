## Week 2

### From Training
This week, I have learned about:
- **File Handling**: Reading, writing in CSV file.
- **PEP-8**:
  - Use snake_case for functions/variables, PascalCase for classes.
  - Add spaces around operators (e.g., `a = b + c`) and after commas.
  - Write clear, concise comments; use docstrings for functions and classes.
  - Place imports at the top, grouped by standard libraries, third-party libraries, and local modules.
  - Separate functions and classes with two blank lines.
  - Use 4 spaces per indentation level.
- **Database Connectivity**:
  - Used SQLite3 library for interacting with SQLite databases.
  - Key Operations:
    - **Connect**: `conn = sqlite3.connect("database.db")` — Opens or creates a database.
    - **Cursor**: `cursor = conn.cursor()` — Executes SQL queries.
    - **Execute Queries**: `cursor.execute("SQL_QUERY")` — Runs SQL commands (e.g., creating tables, inserting data).
    - **Commit**: `conn.commit()` — Saves changes to the database.
    - **Close**: `conn.close()` — Closes the connection.
- **Virtual Environment**: Creating isolated environments for Python projects to manage dependencies.
  - **Create a Virtual Environment**: `python -m venv venv_name`
  - **Activate the Virtual Environment**: `venv_name\Scripts\activate`
- **FastAPI**: A modern web framework for building APIs with Python.
  - Decorators like `@app.get()`, `@app.post()`, `@app.put()`, and `@app.delete()`.
  - To run the App: `uvicorn main:app --reload`
