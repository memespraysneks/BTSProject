from flask import Flask, render_template
from dbconnection import setup_db

import os

def create_app(test=False):
    app = Flask(__name__, instance_relative_config=True)
    
    # secret key for the form
    app.config['SECRET_KEY'] = "secret key"
    
    if test:
        app.config["WTF_CSRF_ENABLED"] = False
        os.environ["FLASKR_TEST_DB"] = "True"

    # Please define imports for pages here, BELOW THE os.environ :) Otherwise i will get mad - Liam
    from register import registerpage
    from editevent import editevent
    from calendarpage import calendarpage
    from adddelete import adddelete
    from login import loginpage

    app.register_blueprint(calendarpage)
    app.register_blueprint(adddelete)
    app.register_blueprint(loginpage)
    app.register_blueprint(registerpage)
    app.register_blueprint(editevent)
    
    with app.app_context():
        setup_db()

    @app.route("/")
    def index():
        return render_template("home.html")

    return app
