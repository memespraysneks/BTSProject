import os
import flask
from flask import Flask, render_template
from adddelete import adddelete



def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    
    # secret key for the form
    app.config['SECRET_KEY'] = "secret key"
    
    app.register_blueprint(adddelete)
    @app.route("/")
    def index():
        return render_template("index.html")
    return app

if __name__ == "__main__":
    create_app()