import flask
from dbconnection import get_db, setup_db
from flaskr import create_app

def setup_db_test():
    setup_db()
    
    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        f'INSERT INTO USERS(USERNAME, USERPASSWORD, USEREMAIL) VALUES(%s,%s,%s)', ('testuser', 'N/A', 'jeff@jeff.test')
        )
    
    cursor.execute(
        f'INSERT INTO EVENTS(EVENTNAME, EVENTDESCRIPTION, EVENTDATE, USERID) VALUES(%s,%s,%s,%s)', ('test','Desc', '2022-01-01', 1)
    )

def test_add_event():
    flask_app = create_app(test=True)
    setup_db_test()

    with flask_app.test_client() as client:
        with client.session_transaction() as ses:
            ses["user_id"] = 1

        response = client.post("/add/2022-01-02?from=UNIT_TEST", data={
            "title": "Test Title234",
            "description": "Test Desc234",
            "time": "12:00:00"
        })

        assert response.status_code == 302
        assert response.get_data(True).count("UNIT_TEST") > 0

def test_delete_event():
    flask_app = create_app(test=True)
    setup_db_test()

    with flask_app.test_client() as client:
        with client.session_transaction() as ses:
            ses["user_id"] = 1

        response = client.get("/deleteEvent/1")

        assert response.status_code == 200
        assert response.get_data(True) == "ok"