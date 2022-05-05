from flask import Flask, redirect, render_template, Blueprint, request, session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from dbconnection import get_db

adddelete = Blueprint('adddelete', __name__)

# create a Form Class
class EventForm(FlaskForm):
    title = StringField("What is your event?", validators=[DataRequired()])
    description = StringField("Please type your event details", validators=[DataRequired()])
    submit = SubmitField("Submit")

#@adddelete.route('/')
#def index():
#    return render_template("home.html")


@adddelete.route('/add/<string:date>', methods=['GET', 'POST'])
def add(date):
    title = None
    description = None
    form = EventForm()

    if form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        db = get_db()
        db.execute(
           f'INSERT INTO EVENTS(EVENTNAME, EVENTDESCRIPTION, EVENTDATE, USERID) VALUES(?,?,?,?)', (title,description, date, session['user_id'])
        )
        db.commit()

        form.title.data = ''
        form.description.data = ''

        redirect_loc = request.args.get("from")
        if redirect_loc is not None:
            return redirect(redirect_loc)

    return render_template("add.html",
        title = title,
        description = description,
        form = form)

@adddelete.route('/update', methods=['GET', 'POST'])
def update():
    pass





