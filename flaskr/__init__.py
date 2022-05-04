import os
import flask
from flask import Flask, render_template
from database import databaseAPI
from login import loginpage

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(databaseAPI)
    app.register_blueprint(loginpage)
    @app.route("/")
    def index():
        return render_template("index.html")
    return app


if __name__ == "__main__":
    create_app()