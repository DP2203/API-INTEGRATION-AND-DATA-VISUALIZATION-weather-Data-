from flask import Flask, render_template, request
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64
import os

# Set up Flask to look for templates in the current directory
app = Flask(__name__, template_folder='.')

API_KEY = "f89460f8fabe4d99866131208250207"  # <-- Your WeatherAPI.com API key
BASE_URL = "http://api.weatherapi.com/v1/current.json"  # WeatherAPI.com current weather endpoint


def fetch_weather_data(api_key, city, base_url):
    if not api_key or api_key == "YOUR_ACTUAL_API_KEY":
        return None, "API key is missing. Please set your WeatherAPI.com API key in app.py."
    params = {
        "key": api_key,
        "q": city
    }
    try:
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        if data.get('error'):
            return None, data['error'].get('message', 'Unknown error from API.')
        return data, None
    except requests.exceptions.RequestException as e:
        return None, f"Error fetching data: {e}"


def process_weather_data(data):
    if data and data.get('current') and data.get('location'):
        temperature = data['current']['temp_c']
        humidity = data['current']['humidity']
        description = data['current']['condition']['text']
        return temperature, humidity, description
    else:
        return None, None, None


def create_visualization(temperature, humidity, city):
    if temperature is not None and humidity is not None:
        df = pd.DataFrame({
            'Weather Metric': ['Temperature (°C)', 'Humidity (%)'],
            'Value': [temperature, humidity]
        })
        plt.figure(figsize=(8, 6))
        sns.barplot(x='Weather Metric', y='Value', data=df, palette='viridis')
        plt.title(f'Weather in {city}')
        plt.ylabel('Value')
        plt.xlabel('Weather Metric')
        plt.ylim(0, max(temperature, humidity) + 10)
        plt.tight_layout()
        img = io.BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        plt.close()
        return base64.b64encode(img.read()).decode()
    else:
        return None


@app.route('/', methods=['GET', 'POST'])
def weather_dashboard():
    city = request.form.get('city', 'Vadodara')
    weather_data, fetch_error = fetch_weather_data(API_KEY, city, BASE_URL)
    temperature, humidity, description = process_weather_data(weather_data)
    img_data = create_visualization(temperature, humidity, city)
    error = None
    if fetch_error:
        error = fetch_error
    elif temperature is None:
        error = f"Could not retrieve weather data for '{city}'. Please try another city."
    return render_template('dashboard.html', city=city, temperature=temperature, humidity=humidity,
                           description=description, img_data=img_data, error=error)


if __name__ == "__main__":
    # Use host='0.0.0.0' for broader access if needed
    app.run(debug=True)