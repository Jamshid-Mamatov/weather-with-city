from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy,request
import os
import requests
import json


key=os.environ['key']
app=Flask(__name__)

@app.route("/")
def home():
    content="weather home"
    return render_template("home.html",content=content)

@app.route("/day")

def day_weather():
    content="daily weather"
    return render_template("day.html",content=content)



if __name__=="__main__":
    app.run(debug=True)
