from flask import render_template
from flask import Blueprint
from flask import request
from flask import g
from flask import redirect
from flask import session
from flask import url_for
from dbconnection import get_db
import sqlite3
import json

loginpage = Blueprint('loginpage', __name__)

@loginpage.route("/login", methods=('GET', 'POST'))
def runTheData ():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None
        user = get_db().execute(
            'SELECT * FROM USERS WHERE USERNAME = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not user['USERPASSWORD'] == password:
            error = 'Incorrect password.'

        if error is None:
            #session.clear()
            #session['user_id'] = user['id']
            return redirect(url_for('index'))

    return render_template('login.html')