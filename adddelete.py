from flask import redirect, render_template, Blueprint, request, session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TimeField
from wtforms.validators import DataRequired
from dbconnection import get_db

adddelete = Blueprint('adddelete', __name__)
db = get_db()

# create a Form Class
class EventForm(FlaskForm):
    title = StringField("What is your event?", validators=[DataRequired()])
    description = StringField("Please type your event details", validators=[DataRequired()])
    time = TimeField("What time is your event?", validators=[DataRequired()])
    submit = SubmitField("Submit")

@adddelete.route('/add/<string:date>', methods=['GET', 'POST'])
def add(date):
    if not "user_id" in session:
        return redirect("/login")

    title = None
    description = None
    form = EventForm()

    if form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        time = form.time.data
        
        db.cursor().execute(
           'INSERT INTO EVENTS(EVENTNAME, EVENTDESCRIPTION, EVENTDATE, USERID) VALUES(%s, %s, %s, %s)', (title,description, f"{date} {time}", session['user_id'])
        )

        form.title.data = ''
        form.description.data = ''

        redirect_loc = request.args.get("from")
        if redirect_loc is not None:
            return redirect(redirect_loc)

    return render_template("add.html",
        title = title,
        description = description,
        form = form)

@adddelete.route("/deleteEvent/<int:eventid>", methods=["GET"])
def deletestuff(eventid):
    db.cursor().execute('DELETE FROM EVENTS WHERE EVENTID = %s AND USERID = %s', (eventid, session["user_id"]))
    return "ok"

