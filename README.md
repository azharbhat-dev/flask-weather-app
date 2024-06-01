# Flask Weather Application

This is a simple Flask web application that provides current weather and a 5-day forecast for a given city or location. The application uses the OpenWeatherMap API to fetch weather data.

## Features

- Get current weather information for a city.
- Get a 5-day weather forecast for a city.
- Get current weather and forecast based on geographical coordinates (latitude and longitude).

## Prerequisites

- Python 3.6 or higher

## Getting Started

Follow these instructions to set up and run the project on your local machine.

### Clone the Repository

```
$ git clone https://github.com/yourusername/flask-weather-app.git
$ cd flask-weather-app
Create a Virtual Environment
Create a virtual environment to manage dependencies.

Copy code
$ python3 -m venv venv
Activate the virtual environment:

On Windows:
Copy code
$ venv\Scripts\activate
On macOS and Linux:

Copy code
$ source venv/bin/activate
Install Dependencies
Install the necessary Python packages using pip.


Copy code
$ pip install -r requirements.txt
Set Up Environment Variables
Create a .env file in the project root directory and add your OpenWeatherMap API key.


Copy code
$ echo "WEATHER_API_KEY=your_openweathermap_api_key" > .env
Run the Application
Run the Flask application.


Copy code
$ python app.py
The application should now be running on http://127.0.0.1:5000.

Usage
Web Interface
Open your web browser and navigate to http://127.0.0.1:5000.
Enter a city name to get the current weather and forecast.
API Endpoints
GET /: Main page with a form to input city name.
POST /location: Get weather by geographical coordinates.
Request Payload:
json
Copy code
{
  "lat": "latitude",
  "lon": "longitude"
}
Response:
json
Copy code
{
  "weather": { ... },
  "forecast": [ ... ],
  "error": "error_message"
}
Logging and Debugging
Logs are enabled for debugging purposes.
Check the terminal output for detailed logs and error messages.
Contributing
Contributions are welcome! Please fork this repository and submit pull requests with your changes.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements
This project uses the OpenWeatherMap API.
perl
Copy code

### Additional Files to Include in Your Repository

Create the following files in your project directory:

1. **`.env.example`**:
   ```plaintext
   WEATHER_API_KEY=your_openweathermap_api_key
requirements.txt:

plaintext
Copy code
Flask==2.0.1
requests==2.25.1
python-dotenv==0.17.0
.gitignore:

plaintext
Copy code
venv/
__pycache__/
.env
*.pyc
*.pyo
Summary of Steps to Run the Project
To summarize, here are all the steps in sequence:

Clone the repository:


Copy code
$ git clone https://github.com/yourusername/flask-weather-app.git
$ cd flask-weather-app
Create and activate a virtual environment:


Copy code
$ python3 -m venv venv
$ source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install dependencies:


Copy code
$ pip install -r requirements.txt
Set up environment variables in a .env file:


Copy code
$ echo "WEATHER_API_KEY=your_openweathermap_api_key" > .env
Run the Flask application:

$ python app.py