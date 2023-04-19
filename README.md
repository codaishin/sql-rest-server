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

Three endpoints `/people-raw`, `/people-modeled` and `/people-tdd` are provided,
which can be accessed directly or via `/docs`.

## Code

The endpoints are implemented in the file [api.py](api.py).

All endpoints are `async` endpoints. For teaching purposes consider using
blocking functions.

The endpoint `/people-raw` returns the database query result. Any type
validation must be done manually.

The endpoint `/people-modeled` defines a pydandic response model, which fastapi
will use to determine, wether the `dict`s contain the correct keys and types.

The endpoint `/people-tdd` showcases, how an endpoint can be written via tdd.

## Testing

Run test via:

```shell
python -m unittest
```

Only the endpoint `/people-tdd` is covered by unit tests to demonstrate a tdd
approach. Of course all the endpoints can be integration tested via fastapis's
`TestClient`. In this case one should introduce a solution to connect to a test
database, which then can be set up in the `setUp` stage of a test.
