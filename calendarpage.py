from asyncio import events
import datetime
import calendar
from flask import Flask, redirect, render_template, url_for, Blueprint, session
from dbconnection import get_db

calendarpage = Blueprint("calendarpage", __name__)

def get_month_data(year, month):
    month_name = datetime.datetime(year, month, 1).strftime("%B")

    calendar.setfirstweekday(6)
    month_calendar = calendar.monthcalendar(year, month)

    return (month_name, month_calendar)

@calendarpage.route("/month")
def month():
    current_date = datetime.date.today()
    return redirect(f"/month/{current_date.year}-{current_date.month}")

@calendarpage.route("/month/<int:year>-<int:month>")
def month_date(year, month):
    if not "user_id" in session:
        return redirect("/login")

    month_name, month_calendar = get_month_data(year, month)
    
    return render_template("month.html", month_id=f"{year}-{month}", month_data=month_calendar, month_name=month_name)

@calendarpage.route("/week")
def week():
    current_date = datetime.date.today()
    return redirect(f"/week/{current_date.year}-{current_date.month}-0")

@calendarpage.route("/week/<int:year>-<int:month>-<int:week>")
def week_date(year, month, week):
    if not "user_id" in session:
        return redirect("/login")

    month_name, month_calendar = get_month_data(year, month)
    week %= len(month_calendar) # Hacky workaround to prevent invalid week

    week_dates = month_calendar[week]
    events = []
    user_id = session["user_id"]
    for row in get_db().execute(f"SELECT * FROM EVENTS WHERE USERID={user_id}"):
        events.append((row["EVENTNAME"], row["EVENTDESCRIPTION"], row["EVENTDATE"]))
    return render_template("week.html", events=events, year=year, month=month, week=week_dates, month_name=month_name, week_num=week)
