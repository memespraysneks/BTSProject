import sqlite3

def setup_db():
    db = get_db()
    with open("database.sql") as sql_file:
        db.cursor().executescript(sql_file.read())

def get_db():
    db = sqlite3.connect("database.db")
    db.row_factory = sqlite3.Row
    return db
