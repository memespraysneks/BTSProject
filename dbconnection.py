import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(":memory:")
        g.db.row_factory = sqlite3.Row
        sql_file = open("database.sql")
        sql_as_string = sql_file.read()
        g.db.cursor().executescript(sql_as_string)

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()
