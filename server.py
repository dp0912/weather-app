from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve

app = Flask(__name__)

@app.route('/')
@app.route('/index')

def index():
    return render_template('index.html')


@app.route('/weather')
def get_weather():
    city = request.args.get('city')

    # check for empty strings or string with only spaces
    if not bool(city.strip()):
        city = "Toronto"

    weather_data = get_current_weather(city)

    # city is not found by API
    if not weather_data['cod'] == 200:
        return render_template('city-not-found.html')
    
    # Extract wind gust if it exists
    windgust = weather_data['wind'].get('gust', 'N/A')
    
    return render_template(
        "weather.html",
        title=weather_data["name"],
        country=f"{weather_data['sys']['country']}",
        status=weather_data["weather"][0]["description"].capitalize(),
        temp=f"{weather_data['main']['temp']:.1f}",
        feels_like=f"{weather_data['main']['feels_like']:.1f}",
        high=f"{weather_data['main']['temp_max']:.1f}",
        low=f"{weather_data['main']['temp_min']:.1f}",
        humidity=f"{weather_data['main']['humidity']}",
        windspeed=f"{weather_data['wind']['speed']}",  
        windgust=windgust,  
    )

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)