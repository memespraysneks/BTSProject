from flask import render_template
from flask import Blueprint
from flask import request
from flask import g
from flask import redirect
from flask import session
from flask import url_for
from dbconnection import get_db
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import sqlite3
import json

loginpage = Blueprint('loginpage', __name__)

class UserForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()], render_kw={"placeholder": "username"})
    password = StringField("Password", validators=[DataRequired()], render_kw={"placeholder": "password"})
    login = SubmitField("Login")

@loginpage.route("/login", methods=('GET', 'POST'))
def login():
    username = None
    password = None
    form = UserForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            
            form.username.data = ''
            form.password.data = ''
            
            error = None
            user = get_db().execute(
                'SELECT * FROM USERS WHERE USERNAME = ?', (username,)
            ).fetchone()


            if user is None:
                error = 'Incorrect username.'
            elif not user['USERPASSWORD'] == password:
                error = 'Incorrect password.'

            if error is None:
                session.clear()
                session['user_id'] = user['USERID']
                return redirect("/month")

    return render_template('login.html',
        username = username,
        password = password,
        form = form)