from flask import render_template
from flask import Blueprint

loginpage = Blueprint('loginpage', __name__)

@loginpage.route("/login")
def runTheData ():
    return render_template("login.html")