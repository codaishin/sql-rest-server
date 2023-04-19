# Example server using native db queries

This provides a small example project exposing a list of people from a database.

## Usage

### Install dependencies

```shell
poetry shell  # activate virtual environment
poetry install  # install dependencies
```

### Migrate database

```shell
python scripts/create_table.py  # creates a person table with 3 entries
```

### Run server

```shell
uvicorn api:app --reload  # starts server on 127.0.0.1:8000
```

### Endpoints

Two endpoints `/people-raw` and `/people-modeled` are provided, which can be
accessed directly or via `/docs`.

## Code

The endpoints are implemented in the file [api.py](api.py).

The endpoint `/people-raw` returns the database query result. Any type
validation must be done manually.

The endpoint `/people-modeled` defines a pydantic response model, which fastapi
will use to determine, wether the `dict`s contain the correct keys and types.
