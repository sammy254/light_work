import os

from cs50 import SQL
from flask import Flask,flash,jsonify,redirect,render_template,request

#configure application
app = Flask(__name__)

#Ensure templates are auto-reloaded
app.config["TEMPALTES_AUTO_RELOADED"] = True

#configure cs50 library to use SQLite database
db = SQL("sqlite:///birthdays.db")

@app.after_request
def after_request(response):
    """Ensure response aren't cached"""
    response.headers["cache-control"] = "no-cache,no-store,must-revalidate"
    response.headers["Expires"] = 0
    response.headers["pragma"] = "no-cache"
    return response
    
@app.route("/",methods["GET","POST"])
def index():
    if request.method == "POST":


        return redirect("/")

    else:
        return render_template("index.html")