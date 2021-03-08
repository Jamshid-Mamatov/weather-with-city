from flask import Flask,render_template,request
from pprint import pprint
import os
import requests
import json
import datetime

key=os.environ['key']
app=Flask(__name__)

@app.route("/")
def home():
    content="weather home"
    return render_template("home.html",content=content)

@app.route("/day")

def day_weather():
    content="daily weather"
    position="/day_weather"
    return render_template("weather.html",content=content,position=position)

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
    
    
    inform ="city not found"
    if r.status_code==200:
        name=data.get("name")
        speed=data['wind']['speed']
        temp=int(data["main"]["temp"]-273.15)
        description=data['weather'][0]['description']
        inform=f"city: {name} <br> wind speed: {speed} <br> temprature: {temp} <br> description:{description}<br> <a href='/'>go to weather home</a>"
    return inform


@app.route("/week")
def week_weather():

    content="5 days weather information "
    position="/fiveDay_inform"
    return render_template("weather.html",content=content,position=position)




@app.route("/fiveDay_inform",methods=["POST"])
def get_week_inform():
    r=request.form
    city=r.get("city")
    url=f"https://api.openweathermap.org/data/2.5/forecast"
    payload={
        "q":city,
        "appid":key
    }
    r=requests.get(url,payload)
    data=r.json()
    dtoday=datetime.date.today()
    dtimedelta=datetime.timedelta(days=1)
    inform="city not found"
    if r.status_code==200:
        name=data['city']['name']
        inform=name+"<br>"
        for i in data['list']:
            dtime=i['dt_txt'][:10]
            if str(dtoday)==dtime:
                # print(dtime)

                speed=i['wind']['speed']
                temp=int(i["main"]["temp"]-273.15)
                description=i['weather'][0]['description']
                inform_data=f"{dtoday}<br>  wind speed: {speed} <br> temprature: {temp} <br> description:{description}<br>"
                inform+=inform_data+"<br>"
                dtoday+=dtimedelta
    return inform + "<a href='/'>go to weather home</a> "      

if __name__=="__main__":
    app.run(debug=True)
