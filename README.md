# Weather Dashboard

This project is a simple weather dashboard built with Flask. It fetches real-time weather data from the OpenWeatherMap API and visualizes temperature and humidity using Matplotlib and Seaborn.

## Features
- Enter any city to view its current weather.
- Visualizes temperature and humidity as a bar chart.
- Displays weather description and handles errors for invalid cities or missing API key.

## Setup Instructions

### 1. Get an OpenWeatherMap API Key
- Sign up for a free account at [OpenWeatherMap](https://home.openweathermap.org/users/sign_up).
- Go to the API keys section and copy your API key.
- Open `app.py` and replace the placeholder with your API key:
  ```python
  API_KEY = "YOUR_ACTUAL_API_KEY"
  ```

### 2. Install Dependencies
Run the following command in your project directory:
```bash
pip install flask requests pandas matplotlib seaborn
```

### 3. Run the App
Start the Flask server with:
```bash
python app.py
```

### 4. Use the Dashboard
- Open your browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
- Enter a city name and click "Get Weather" to view the weather data and visualization.

## Project Structure
```
Project 1/
  ├── app.py
  ├── dashboard.html
  └── README.md
```

## Notes & Troubleshooting
- If you enter an invalid city, an error message will be displayed.
- If you forget to set your API key, the dashboard will prompt you.
- The dashboard uses Bootstrap for basic styling.
- If you get a template error, make sure `dashboard.html` is in the same directory as `app.py` (the project root).
- If you want to access the app from another device, change `app.run(debug=True)` to `app.run(debug=True, host='0.0.0.0')` in `app.py`.

---
Enjoy your weather dashboard! 