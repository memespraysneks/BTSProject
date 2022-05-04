from flask import Flask, redirect, render_template, url_for
from calendarpage import calendarpage

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(calendarpage)
    @app.route("/")
    def index():
        return render_template("index.html")

    return app

if __name__ == "__main__":
    create_app()