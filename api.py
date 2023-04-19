"""API"""
import sqlite3
from typing import Iterable

from fastapi import FastAPI
from pydantic import BaseModel

from validators import has_tuple_int_str_str

app = FastAPI()


def get_people() -> list:
    """get people from database"""

    connection = sqlite3.connect("db.sqlite3")
    cursor = connection.cursor()
    query = cursor.execute("SELECT uid, first_name, last_name FROM person")
    return query.fetchall()


@app.get("/people-raw")
async def people_raw() -> list[tuple[int, str, str]]:
    """Get all people from the database

    fastapi's documentation/validation will only pick up
    that we want to return a list of `tuple`s with 3 `string`s
    """

    data = get_people()

    if not has_tuple_int_str_str(data):
        raise TypeError("data from db had unexpected format")

    return data


class Person(BaseModel):
    """person"""

    uid: int
    first_name: str
    last_name: str


@app.get("/people-modeled", response_model=list[Person])
async def people_modeled() -> Iterable[dict]:
    """Get all people from the database

    fastapi's documentation/validation will validate the
    list of `dict`s to be in line with a list of `Person` elements
    """

    return (
        {"uid": uid, "first_name": first_name, "last_name": last_name}
        for (uid, first_name, last_name) in get_people()
    )
