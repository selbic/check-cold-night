# Check Cold Night

This project checks the weather forecast and sends a notification if a cold night is predicted. It uses GitHub Actions to automate this process daily.

## How It Works

1. **Scheduled Workflow**:  
   The workflow is set to run **daily at 9:00 AM UTC**. It triggers a Python script that checks the weather using the OpenWeather API.

2. **Secrets Management**:  
   API keys for OpenWeather and Pushbullet are stored securely as GitHub Secrets, ensuring sensitive information is kept safe.

3. **Automated Notifications**:  
   If the forecast indicates a cold night, a notification is sent via Pushbullet.

## GitHub Actions

The workflow is defined in `.github/workflows/weather-check.yml` and performs the following tasks:

1. Runs at the scheduled time using `cron`.
2. Sets up the Python environment, installs dependencies, and runs the weather-check script.
3. Utilizes GitHub Secrets for securely accessing API keys.

This setup ensures you’re notified about cold weather without any manual checks, running entirely on GitHub’s infrastructure.

## Requirements

- Python 3.x
- OpenWeather API key (free)
- Pushbullet API key (free)

## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/check-cold-night.git

2. Install the required dependencies:
   ```bash   
   pip install -r requirements.txt

3. Create a .env file and add your API keys:
   ```bash
    makefile
    OPEN_WEATHER_API=your_open_weather_api_key
    PUSHBULLET_API_KEY=your_pushbullet_api_key
