import _sqlite3 as sqlite3
from flask import Blueprint

databaseAPI = Blueprint('databaseAPI', __name__)

@databaseAPI.route("/secretDatabase")
def runTheData ():
    connection = sqlite3.connect(":memory:")

    cursor = connection.cursor()

    sql_file = open("database.sql")
    sql_as_string = sql_file.read()
    cursor.executescript(sql_as_string)
    listofusers = []
    for row in cursor.execute("SELECT * FROM USERS"):
        listofusers+= row
    return str(listofusers)