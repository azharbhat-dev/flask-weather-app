from flask import Flask, render_template, request, jsonify
import requests
import os
from datetime import datetime
import logging

app = Flask(__name__)

# Enable logging
logging.basicConfig(level=logging.DEBUG)

# Correctly retrieve the API key from environment variables
API_KEY = os.getenv('API KEY')

if not API_KEY:
    logging.error("API Key is not set. Make sure to set the WEATHER_API_KEY environment variable.")
else:
    logging.debug(f"API Key loaded: {API_KEY}")
    print(f"API Key: {API_KEY}")  # Print the API key for verification

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    forecast_data = None
    error_message = None
    if request.method == 'POST':
        city = request.form['city']
        weather_data, forecast_data, error_message = get_weather(city)
    return render_template('index.html', weather=weather_data, forecast=forecast_data, error=error_message)

@app.route('/location', methods=['POST'])
def location():
    lat = request.json.get('lat')
    lon = request.json.get('lon')
    weather_data, forecast_data, error_message = get_weather_by_location(lat, lon)
    return jsonify(weather=weather_data, forecast=forecast_data, error=error_message)

def get_weather(city):
    try:
        logging.debug(f"Getting weather for city: {city}")
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
        forecast_url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric'
        logging.debug(f"Weather API URL: {url}")
        logging.debug(f"Forecast API URL: {forecast_url}")
        response = requests.get(url)
        forecast_response = requests.get(forecast_url)
        logging.debug(f"Weather API response status code: {response.status_code}")
        logging.debug(f"Forecast API response status code: {forecast_response.status_code}")
        logging.debug(f"Weather API response: {response.text}")
        logging.debug(f"Forecast API response: {forecast_response.text}")
        if response.status_code == 200 and forecast_response.status_code == 200:
            weather = parse_weather_data(response.json())
            forecast = parse_forecast_data(forecast_response.json())
            return weather, forecast, None
        else:
            error_msg = response.json().get('message', 'City not found')
            return None, None, error_msg
    except Exception as e:
        logging.error(f"Error getting weather data: {e}")
        return None, None, str(e)

def get_weather_by_location(lat, lon):
    try:
        logging.debug(f"Getting weather for coordinates: lat={lat}, lon={lon}")
        url = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric'
        forecast_url = f'http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}&units=metric'
        logging.debug(f"Weather API URL: {url}")
        logging.debug(f"Forecast API URL: {forecast_url}")
        response = requests.get(url)
        forecast_response = requests.get(forecast_url)
        logging.debug(f"Weather API response status code: {response.status_code}")
        logging.debug(f"Forecast API response status code: {forecast_response.status_code}")
        logging.debug(f"Weather API response: {response.text}")
        logging.debug(f"Forecast API response: {forecast_response.text}")
        if response.status_code == 200 and forecast_response.status_code == 200:
            weather = parse_weather_data(response.json())
            forecast = parse_forecast_data(forecast_response.json())
            return weather, forecast, None
        else:
            error_msg = response.json().get('message', 'Location not found')
            return None, None, error_msg
    except Exception as e:
        logging.error(f"Error getting weather data by location: {e}")
        return None, None, str(e)

def parse_weather_data(data):
    return {
        'city': data['name'],
        'temperature': data['main']['temp'],
        'description': data['weather'][0]['description'],
        'humidity': data['main']['humidity'],
        'pressure': data['main']['pressure'],
        'wind_speed': data['wind']['speed'],
        'sunrise': datetime.fromtimestamp(data['sys']['sunrise']).strftime('%Y-%m-%d %H:%M:%S'),
        'sunset': datetime.fromtimestamp(data['sys']['sunset']).strftime('%Y-%m-%d %H:%M:%S'),
        'icon': data['weather'][0]['icon']
    }

def parse_forecast_data(data):
    forecast = []
    for entry in data['list']:
        forecast.append({
            'date': entry['dt_txt'],
            'temperature': entry['main']['temp'],
            'description': entry['weather'][0]['description'],
            'icon': entry['weather'][0]['icon']
        })
    return forecast

if __name__ == '__main__':
    app.run(debug=True)
