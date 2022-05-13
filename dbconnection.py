import sqlite3
import os
from flask import current_app

def setup_db():
    if current_app.config["TEST_DB"]:
        os.remove("database_test.db")

    db = get_db()
    with open("database.sql") as sql_file:
        db.cursor().executescript(sql_file.read())

def get_db():
    db = sqlite3.connect("database.db" if not current_app.config["TEST_DB"] else "database_test.db")
    db.row_factory = sqlite3.Row
    return db
