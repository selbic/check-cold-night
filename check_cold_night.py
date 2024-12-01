import os
import requests
from datetime import datetime, timedelta
import pytz

# OpenWeatherMap API-Konfiguration
API_KEY = os.getenv('OPEN_WEATHER_API')  # The environment variable that holds the API key
if not API_KEY:
    print("API key not set.")
    exit(1)
    
LOCATION = 'Berlin,de'                  # Stadt und Land
UNITS = 'metric'                        # Metrische Einheiten (°C)
WEATHER_URL = f'http://api.openweathermap.org/data/2.5/forecast?q={LOCATION}&appid={API_KEY}&units={UNITS}'

# Pushbullet API-Konfiguration
PUSHBULLET_API_TOKEN = os.getenv('PUSHBULLET_API_KEY') # Ersetze mit deinem API-Token
PUSHBULLET_URL = 'https://api.pushbullet.com/v2/pushes'

def get_weather_forecast():
    """Ruft die Wettervorhersage von OpenWeatherMap ab."""
    response = requests.get(WEATHER_URL)
    response.raise_for_status()
    return response.json()

def send_push_notification(title, message):
    """Sendet eine Push-Benachrichtigung über Pushbullet."""
    headers = {
        'Access-Token': PUSHBULLET_API_TOKEN,
        'Content-Type': 'application/json'
    }
    data = {
        'type': 'note',
        'title': title,
        'body': message
    }
    response = requests.post(PUSHBULLET_URL, headers=headers, json=data)
    response.raise_for_status()

def check_for_cold_night():
    """Überprüft die Wettervorhersage auf Temperaturen unter -5°C in der kommenden Nacht."""
    forecast = get_weather_forecast()
    timezone = pytz.timezone('Europe/Berlin')  # Zeitzone für Deutschland
    current_time = datetime.now(timezone)
    next_night_start = (current_time + timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)

    for item in forecast['list']:
        forecast_time = datetime.fromtimestamp(item['dt'], tz=timezone)
        if next_night_start <= forecast_time < next_night_start + timedelta(hours=6):  # Nachtstunden (00:00 - 06:00)
            temp = item['main']['temp']
            if temp < 100:
                send_push_notification(
                    title="Kalte Nachtwarnung!",
                    message=f"In der kommenden Nacht wird es {temp}°C kalt. Bring die Pflanzen rein!"
                )
                break

if __name__ == '__main__':
    check_for_cold_night()


