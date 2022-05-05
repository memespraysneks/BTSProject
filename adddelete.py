from flask import Flask, render_template, Blueprint
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


adddelete = Blueprint('adddelete', __name__)


# create a Form Class
class EventForm(FlaskForm):
    title = StringField("What is your event?", validators=[DataRequired()])
    submit = SubmitField("Submit")

#@adddelete.route('/')
#def index():
#    return render_template("home.html")


@adddelete.route('/add', methods=['GET', 'POST'])
def add():
    title = None
    form = EventForm()

    if form.validate_on_submit():
        title = form.title.data
        form.title.data = ''

    return render_template("add.html",
        title = title,
        form = form)




