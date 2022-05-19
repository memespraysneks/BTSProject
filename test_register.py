import flask
from dbconnection import get_db, setup_db
from flaskr import create_app

def setup_db_test():
    setup_db()


def test_register():
    flask_app = create_app(test=True)
    setup_db_test()

    with flask_app.test_client() as client:
        with client.session_transaction() as ses:
            ses.clear()

        response = client.post("/register", data={
            "email": "uniqueemail@email.com",
            "username": "testusername",
            "password": "password123",
            "password2": "password123"
        })

        assert response.status_code == 302
        assert response.get_data(True).count("month") > 0
        with client.session_transaction() as ses:
            assert ses["user_id"] == 1

