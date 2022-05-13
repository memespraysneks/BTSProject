from flask import redirect, render_template, Blueprint, request, session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from dbconnection import get_db

editevent = Blueprint('editevent', __name__)

# create a Form Class
class EditForm(FlaskForm):
    title = StringField("Event Title", validators=[DataRequired()])
    description = StringField("Event Details", validators=[DataRequired()])
    submit = SubmitField("Edit")

@editevent.route('/edit/<int:eventid>', methods=['GET', 'POST'])
def edit(eventid):

    form = EditForm()
    db = get_db()

    if form.validate_on_submit():
        db.execute(f"UPDATE EVENTS SET EVENTNAME = ?, EVENTDESCRIPTION = ? WHERE USERID={session['user_id']} AND EVENTID={eventid}", (form.title.data, form.description.data))
        db.commit()

        redirect_loc = request.args.get("from")
        if redirect_loc is not None:
            return redirect(redirect_loc)

    else:
        eventdetails = db.execute(f"SELECT EVENTNAME, EVENTDESCRIPTION FROM EVENTS WHERE USERID={session['user_id']} AND EVENTID={eventid}").fetchone()
        form.title.data = eventdetails["EVENTNAME"]
        form.description.data = eventdetails["EVENTDESCRIPTION"]

    return render_template("edit.html",
        form = form)











