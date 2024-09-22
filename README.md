# Weather App

## Overview
This Weather App allows users to get current weather conditions for a specified city. The app uses the OpenWeatherMap API to fetch weather data and displays it on a web interface. The application is built using Python with Flask for the backend and HTML/CSS for the frontend.

## Features
- Get current weather conditions for any city.
- Display temperature, weather description, wind speed, and more.
- Handle cases where the city is not found.
- Responsive design for different screen sizes.

## Requirements
- **Python 3.6 or higher**
- **Flask**
- **Requests**
- **Python-dotenv**
- **Waitress**

## Usage
1. Open the app in your web browser.
2. Enter the name of a city in the input field and click "Submit".
3. The current weather information for the city will be displayed.

## Code Structure
- `app.py`: The main Python script that sets up the Flask application and routes.
- `weather.py`: Contains the `get_current_weather` function to fetch weather data from the OpenWeatherMap API.
- `templates/`: Directory containing HTML templates.
  - `index.html`: The homepage where users can enter a city name.
  - `weather.html`: Displays the weather information.
  - `city-not-found.html`: Shown when the city is not found.
- `static/styles/`: Contains CSS files for styling the web pages.
  - `style.css`: Styles for the weather information and forms.

## Notes
- Ensure that your API key is correctly set in the `.env` file.
- The `app.py` file uses Waitress for serving the Flask app. If deploying, consider using a production-ready server.
