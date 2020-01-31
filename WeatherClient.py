import requests

answer = 'Y'
while True:
    if str.upper(answer) == 'Y':

        city_name = input("Enter City Name to Get Its Temperature Note first letter is capital:\n")
        r = requests.get(url="http://127.0.0.1:5000/weather/{}".format(city_name))

        # r.json.get(put here the key of api inside the jsonify in WeatherApiMsattar)
        print("{} Temperature is {}".format(city_name, r.json().get(city_name)))

        print("\r")
        print("THANK YOU !!! \U0001F603")
        answer = input("Do it Again??  (Y , N) :  ")
        print("\r")
    else:
        break
