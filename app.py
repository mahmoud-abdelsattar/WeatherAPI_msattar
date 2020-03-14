"""
WEATHER API Using City Names!!!
"""
import random
from flask import jsonify, request, Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Weather API by Mahmoud Abd Elsattar !</h1>'


# Key is city name
# Value is temperature
cities_temperatures = {'Al Ain': 33, 'Amsterdam': 19, 'Toronto': 21,
                       'Roma': 22, 'Alexandria': 29, 'Athens': 20,
                       'Cairo': 30, 'Berlin': 18, 'Paris': 19,
                       'Madrid': 18, 'Barcelona': 20, 'Istanbul': 24}


@app.route('/weather/<city>')
def get_temperature(city):
    """get weather temperature by city
    """
    res = ''
    try:

        temp_response = cities_temperatures.get(city)
        if temp_response is not None:
            # return the response parsed in a json object
            # key is temperature for clients to use it to get the city temperature
            return jsonify({city: temp_response})
        else:
            return jsonify({"temperature": "This is not existed in our database Sorry for that and good luck next time!!!! "
                                           "\U0001F603."})
    except:
        return jsonify("Something went wrong!!!")

    # return the response parsed in a json object
    # return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)
    #app.run()
