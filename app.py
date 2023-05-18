import requests
from flask import Flask , render_template ,request
app = Flask(__name__)

@app.route("/")
def hello():
  url='http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=59ad25c75743b2cb343f4c299e429aa1'
  city='gwalior'
  r=requests.get(url.format(city)).json()
  weather = {
            'city' : city,
            'temperature' : round((((r['main']['temp'])-32)*5)/9, 1),
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
            'humidity' : r['main']['humidity'],
            'speed' : r['wind']['speed']
        }
  print(weather)
  return render_template('weather.html', weather=weather)
  
@app.route("/search")
def search():
  url='http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=59ad25c75743b2cb343f4c299e429aa1'
  city=request.args['city']
  r=requests.get(url.format(city)).json()
  weather = {
            'city' : city,
            'temperature' : round((((r['main']['temp'])-32)*5)/9, 1) ,
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
            'humidity' : r['main']['humidity'],
            'speed' : r['wind']['speed']
        }
  print(weather)
  return render_template('weather.html',weather=weather)

@app.route("/advancesearch")
def advancesearch():
  url='http://api.openweathermap.org/data/2.5/forecast?q={}&units=metric&appid=59ad25c75743b2cb343f4c299e429aa1'
  city=request.args['forecast']
  r=requests.get(url.format(city)).json()
  print(len(r['list']))
  weatherdata=[]
  for i in range(len(r['list'])):
    weather = {
            'city' : city,
            'dAt':r['list'][i]['dt_txt'],
            'temperature' : r['list'][i]['main']['temp'],
            'description' : r['list'][i]['weather'][0]['description'],
            'icon' : r['list'][i]['weather'][0]['icon'],
            'humidity' : r['list'][i]['main']['humidity'],
            'speed' : r['list'][i]['wind']['speed']
        }
    weatherdata.append(weather)
        
    print(weatherdata)
  return render_template('advancesearch.html',weather=weatherdata)

if __name__ == "__main__":
  app.run()