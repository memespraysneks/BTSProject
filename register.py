from urllib.parse import uses_params
from flask import render_template
from flask import Blueprint
from flask import request
from flask import g
from flask import redirect
from flask import session
from flask import url_for
from dbconnection import get_db
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, PasswordField
from wtforms.validators import DataRequired, EqualTo
import sqlite3
import json

class RegisterForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired()])
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired(), EqualTo("password2", message="Passwords must match!")])
    password2 = PasswordField("Confirm Password", validators=[DataRequired()])
    submit = SubmitField("Submit")

registerpage = Blueprint('registerpage', __name__)

#TODO : SQL ERROR HANDLING
@registerpage.route("/register", methods=('GET', 'POST'))
def runTheData ():
    form = RegisterForm()

    if form.validate_on_submit():
        email = form.email.data
        username = form.username.data
        password = form.password.data
        
        print(email, username, password)
        db = get_db()
        cursor = db.execute(
            f'INSERT INTO USERS(USERNAME, USERPASSWORD) VALUES(?,?)', (username, password)
        )
        db.commit()

        new_user_id = cursor.lastrowid
        session.clear()
        session["user_id"] = new_user_id

        return redirect("/month")

    return render_template('register.html', form=form)