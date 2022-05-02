import os
import flask
from flask import Flask, render_template


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    @app.route("/")
    def index():
        return render_template("index.html")
    
    return app

if __name__ == "__main__":
    create_app()