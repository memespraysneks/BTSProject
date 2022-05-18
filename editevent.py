from flask import redirect, render_template, Blueprint, request, session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TimeField
from wtforms.validators import DataRequired
from dbconnection import get_db

editevent = Blueprint('editevent', __name__)
db = get_db()

# create a Form Class
class EditForm(FlaskForm):
    title = StringField("Event Title", validators=[DataRequired()])
    description = StringField("Event Details", validators=[DataRequired()])
    time = TimeField("Event Time", validators=[DataRequired()])
    submit = SubmitField("Edit")

@editevent.route('/edit/<int:eventid>', methods=['GET', 'POST'])
def edit(eventid):

    form = EditForm()
    cursor = db.cursor()

    if form.validate_on_submit():
        cursor.execute(f"UPDATE EVENTS SET EVENTNAME = %s, EVENTDESCRIPTION = %s, EVENTDATE = DATE_ADD(CAST(CAST(EVENTDATE AS DATE) AS DATETIME), INTERVAL %s HOUR_SECOND)  WHERE USERID={session['user_id']} AND EVENTID={eventid}", (form.title.data, form.description.data, form.time.data))

        redirect_loc = request.args.get("from")
        if redirect_loc is not None:
            return redirect(redirect_loc)

    else:

        cursor.execute(f"SELECT EVENTNAME, EVENTDESCRIPTION, EVENTDATE FROM EVENTS WHERE USERID={session['user_id']} AND EVENTID={eventid}")
        eventdetails = cursor.fetchone()
        form.title.data = eventdetails[0]
        form.description.data = eventdetails[1]
        print(eventdetails[2])
        form.time.data = eventdetails[2]

    return render_template("edit.html",
        form = form)











