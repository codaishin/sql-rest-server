"""create person table"""

import sqlite3

CREATE = """
CREATE TABLE person(
    uid INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name NVARCHAR,
    last_name NVARCHAR
);
"""

INSERT = "INSERT INTO person (first_name, last_name) VALUES(?, ?)"

PEOPLE = [
    ("Harry", "Haller"),
    ("James", "Bond"),
    ("Marry", "Sue"),
]


if __name__ == "__main__":
    connection = sqlite3.connect("db.sqlite3")
    cursor = connection.cursor()

    cursor.execute(CREATE)
    connection.commit()

    cursor.executemany(INSERT, PEOPLE)
    connection.commit()
