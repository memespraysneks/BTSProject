import MySQLdb
import os
from flask import current_app

def setup_db():
    if current_app.config["TEST_DB"]:
        os.remove("database_test.db")

    db = get_db()
    with open("database.sql") as sql_file:
        db.cursor().execute(sql_file.read())


def get_db():
    db = MySQLdb.connect(host="db-mysql-tor1-88382-do-user-11598939-0.b.db.ondigitalocean.com", user="doadmin", passwd="AVNS_oXpa1nDA3uxs4LM", db="defaultdb", port=25060, autocommit=True)
    #db.row_factory = MySQLdb.Row
    return db
