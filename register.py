from flask import render_template, Blueprint, redirect, session
from dbconnection import get_db
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, PasswordField
from wtforms.validators import DataRequired, EqualTo
from passlib.hash import sha256_crypt

class RegisterForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired()])
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired(), EqualTo("password2", message="Passwords must match!")])
    password2 = PasswordField("Confirm Password", validators=[DataRequired()])
    submit = SubmitField("Submit")

registerpage = Blueprint('registerpage', __name__)
db = get_db()

@registerpage.route("/register", methods=('GET', 'POST'))
def runTheData():
    form = RegisterForm()

    if form.validate_on_submit():
        email = form.email.data
        username = form.username.data
        password = form.password.data
        hashedpassword = sha256_crypt.hash(password)
        
        cur = db.cursor() 
        cur.execute(f"SELECT COUNT(*) FROM USERS WHERE USERNAME = %s ", (username,)) 
        numberOfRows = cur.fetchone()[0]

        if numberOfRows == 0:
            cur.execute(
            'INSERT INTO USERS(USERNAME, USERPASSWORD, USEREMAIL) VALUES(%s,%s,%s)', (username, hashedpassword, email)
            )
        else:
            return redirect("/register")

        new_user_id = cur.lastrowid
        session.clear()
        session["user_id"] = new_user_id

        return redirect("/month")

    return render_template('register.html', form=form)
