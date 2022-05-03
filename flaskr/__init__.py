import os
import flask
from flask import Flask, redirect, render_template, url_for
import datetime
import calendar


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/month")
    def month():
        return redirect(f"/month/{datetime.date.today().isoformat()}")

    @app.route("/month/<date>")
    def month_date(date):
        calendar_date = datetime.date.fromisoformat(date)
        calendar.setfirstweekday(6)
        month_calendar = calendar.monthcalendar(calendar_date.year, calendar_date.month)
        return render_template("month.html", month_data=month_calendar, month_name=calendar_date.strftime("%B"))

    return app

if __name__ == "__main__":
    create_app()