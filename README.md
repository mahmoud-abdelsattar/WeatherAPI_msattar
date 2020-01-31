# WeatherAPI_msattar
REST API example application
This is a city-temperature example of a application providing a API to get the temperature.

WeatherClient.py runs a simplistic test and generates of API.

When you run the test you can choose one of these city to see the API proccess.

heroku link:
https://weatherapimsattar.herokuapp.com/

The API to the example app is described below.

Get Weather Temperature for non existed city:
Request
GET

http://127.0.0.1:5000/weather/BokaBoka

Response
{"temperature": "not is not existed in our database Sorry For good luck next time!!!!}

+++++++++++++++++++++++++++++++++++++

Get Weather Temperature for existed City:
Request
GET

http://127.0.0.1:5000/weather/Cairo

Response
{"Cairo":30}
