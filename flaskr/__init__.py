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
        current_date = datetime.date.today()
        return redirect(f"/month/{current_date.year}-{current_date.month}")

    @app.route("/month/<int:year>-<int:month>")
    def month_date(year, month):
        month_name = datetime.datetime(year, month, 1).strftime("%B")

        calendar.setfirstweekday(6)
        month_calendar = calendar.monthcalendar(year, month)
        
        return render_template("month.html", month_id=f"{year}-{month}", month_data=month_calendar, month_name=month_name)

    @app.route("/week")
    def week():
        current_date = datetime.date.today()
        return redirect(f"/week/{current_date.year}-{current_date.month}-0")

    @app.route("/week/<int:year>-<int:month>-<int:week>")
    def week_date(year, month, week):
        month_name = datetime.datetime(year, month, 1).strftime("%B")

        calendar.setfirstweekday(6)
        month_calendar = calendar.monthcalendar(year, month)
        week %= len(month_calendar) 

        week_dates = month_calendar[week] # Hacky workaround to prevent invalid week
        return render_template("week.html", week=week_dates, month_name=month_name, week_num=week)

    return app

if __name__ == "__main__":
    create_app()