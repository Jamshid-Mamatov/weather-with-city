from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
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

@app.route("/day_weather",methods=['POST'])
def get_day_city():
    r=request.form
    city=r.get("city")
    # print(r.get("city"))
    url=f"https://api.openweathermap.org/data/2.5/weather"
    payload={
        "q":city,
        "appid":key
    }
    r=requests.get(url,payload)
    data=r.json()
    # print(data)
    inform ="city not found"
    if r.status_code==200:
        name=data.get("name")
        speed=data['wind']['speed']
        temp=int(data["main"]["temp"]-273.15)
        description=data['weather'][0]['description']
        inform=f"city: {name} <br> wind speed: {speed} <br> temprature: {temp} <br> description:{description}<br> <a href='/'>go to weather home</a>"
    return inform

if __name__=="__main__":
    app.run(debug=True)
