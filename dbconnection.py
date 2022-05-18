import MySQLdb
import os

def setup_db():
    db = get_db()
    if os.environ.get("FLASKR_TEST_DB"):
        db.cursor().execute("DROP TABLE IF EXISTS EVENTS, USERS;")

    
    with open("database.sql") as sql_file:
        db.cursor().execute(sql_file.read())


def get_db(): 
    database_name = "defaultdb" if not os.environ.get("FLASKR_TEST_DB") else "test_db"
    db = MySQLdb.connect(host="db-mysql-tor1-88382-do-user-11598939-0.b.db.ondigitalocean.com", user="doadmin", passwd="AVNS_oXpa1nDA3uxs4LM", db=database_name, port=25060, autocommit=True)
    #db.row_factory = MySQLdb.Row
    return db
