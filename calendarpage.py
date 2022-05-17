from asyncio import events
import datetime
import calendar
from flask import Flask, redirect, render_template, url_for, Blueprint, session
from dbconnection import get_db

calendarpage = Blueprint("calendarpage", __name__)

db = get_db()

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
    user_id = session["user_id"]
    events = get_user_events(user_id)
    event_counts = get_user_events_by_date(user_id=user_id)
    
    return render_template("week.html", event_counts=event_counts, events=events, year=year, month=month, week=week_dates, month_name=month_name, week_num=week)

def get_user_events_by_date(user_id):
    events = {}
    cursor = db.cursor()
    cursor.execute(f"SELECT EVENTDATE, COUNT(*) as COUNT FROM EVENTS WHERE USERID={user_id} GROUP BY EVENTDATE")
    for row in cursor.fetchall():
        events[f"{row[0].year}-{row[0].month}-{row[0].day}"] = row[1]

    return events

def get_user_events(user_id):
    events = []
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM EVENTS WHERE USERID={user_id}")
    for row in cursor.fetchall():
        split_date = row[3]
        events.append((row[1], row[2], split_date.year, split_date.month, split_date.day, row[0]))
    
    return events

