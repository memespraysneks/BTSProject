import os
import flask
from flask import Flask, render_template
from database import databaseAPI

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(databaseAPI)
    @app.route("/")
    def index():
        return render_template("index.html")
    return app


if __name__ == "__main__":
    create_app()