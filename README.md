# Check Cold Night

This project checks the weather forecast and sends a notification if a cold night is predicted. It uses GitHub Actions to automate this process daily. The underlying reason is that I need to put the plants into the garage once a temperature below -4 degrees Celsius is expected. If this works, I would receive a warning on my Android phone the preceding day at 10am UTC based on Open Weather forecasts. 

## How It Works

1. **Scheduled Workflow**:  
   The workflow is set to run **daily at 10:00 AM UTC**. It triggers a Python script that checks the weather using the OpenWeather API.

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

2. Push to your GitHub:
   After cloning, push it to your own GitHub repository:

   ```bash
   cd check-cold-night
   git remote set-url origin https://github.com/yourusername/check-cold-night.git
   git push -u origin main

3. Set up GitHub Secrets:
   In your GitHub repository, go to Settings > Secrets and variables > Actions and add the following secrets:
   ```bash
   OPEN_WEATHER_API: Your OpenWeather API key.
   PUSHBULLET_API_KEY: Your Pushbullet API key.

4. Adjust Cron Schedule (optional):
   You can adjust the cron schedule in the .github/workflows/weather-check.yml file if you want the script to run at a different time.
