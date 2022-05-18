import flask
from dbconnection import get_db, setup_db
from flaskr import create_app
from passlib.hash import sha256_crypt

def setup_db_test():
    setup_db()
    
    db = get_db()
    cursor = db.cursor()

    passwd = sha256_crypt.hash("testpassword123")

    cursor.execute(
        f'INSERT INTO USERS(USERNAME, USERPASSWORD, USEREMAIL) VALUES(%s,%s,%s)', ('testuser', passwd, 'jeff@jeff.test')
        )


def test_login():
    flask_app = create_app(test=True)
    setup_db_test()

    with flask_app.test_client() as client:
        with client.session_transaction() as ses:
            ses.clear()

        response = client.post("/login", data={
            "username": "testuser",
            "password": "testpassword123",
        })

        assert response.status_code == 302
        with client.session_transaction() as ses:
            assert ses["user_id"] == 1

