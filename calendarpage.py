import datetime
import calendar
from flask import redirect, render_template, Blueprint, session
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

    user_id = session["user_id"]
    month_name, month_calendar = get_month_data(year, month)
    last_month, next_month = get_last_next_month(year, month)
    event_counts = get_user_events_by_date(user_id=user_id)
    
    return render_template("month.html", event_counts=event_counts, month_id=f"{year}-{month}", month_data=month_calendar, month_name=month_name, year=year, last_month=last_month, next_month=next_month)

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

    last_week, next_week = get_last_next_week(year, month, week)
    
    return render_template("week.html", event_counts=event_counts, events=events, year=year, month=month, week=week_dates, month_name=month_name, week_num=week, last_week=last_week, next_week=next_week)

@calendarpage.route("/todo")
def show_todo():
    if not "user_id" in session:
        return redirect("/login")

    user_id = session["user_id"]
    events = get_user_events(user_id)
    event_counts = get_user_events_by_date(user_id=user_id)
    
    return render_template("todo.html", event_counts=event_counts, events=events)


def get_user_events_by_date(user_id):
    events = {}
    cursor = db.cursor()
    cursor.execute("SELECT CAST(EVENTDATE AS DATE), COUNT(*) as COUNT FROM EVENTS WHERE USERID=%s GROUP BY CAST(EVENTDATE AS DATE)", (user_id,))
    for row in cursor.fetchall():
        events[f"{row[0].year}-{row[0].month}-{row[0].day}"] = row[1]

    return events

def get_user_events(user_id):
    events = []
    cursor = db.cursor()
    cursor.execute("SELECT * FROM EVENTS WHERE USERID=%s ORDER BY EVENTDATE", (user_id,))
    for row in cursor.fetchall():
        split_date = row[3]
        events.append((row[1], row[2], split_date.year, split_date.month, split_date.day, row[0], row[3].strftime("%I:%M %p")))
    
    return events

def get_last_next_week(year, month, week):
    name, mcal = get_month_data(year, month)

    last_month = month
    next_month = month
    last_month_year = year
    next_month_year = year
    next_week = week + 1
    last_week = week - 1

    if next_week >= len(mcal):
        next_month += 1
        next_week = 0

        if next_month > 12:
            next_month_year += 1
            next_month = 1
    if last_week < 0:
        last_month -= 1
        if last_month < 1:
            last_month_year -= 1
            last_month = 12

        lname, lmcal = get_month_data(last_month_year, last_month)
        last_week = len(lmcal) - 1
    
    return f"{last_month_year}-{last_month}-{last_week}", f"{next_month_year}-{next_month}-{next_week}"

def get_last_next_month(year, month):
    last_month = month - 1
    next_month = month + 1
    last_month_year = year
    next_month_year = year

    if next_month > 12:
        next_month_year += 1
        next_month = 1
    if last_month < 1:
        last_month_year -= 1
        last_month = 12
    
    return f"{last_month_year}-{last_month}", f"{next_month_year}-{next_month}"