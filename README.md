# Check Cold Night

A Python script that checks the weather forecast for a particularly cold night and sends a Pushbullet notification when the temperature is low.

## Features

- Fetches weather data from OpenWeatherMap API.
- Sends a Pushbullet notification when temperature falls below a defined threshold.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/check-cold-night.git
    cd check-cold-night
    ```

2. Set up a virtual environment and install dependencies:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. Set up your API keys in your GitHub Secrets for deployment using GitHub Actions.

## Usage

1. Run the script:
    ```bash
    python check_cold_night.py
    ```

2. The script will check the weather and notify you if the temperature falls below your set threshold.

## Contributing

Feel free to fork this repository and make improvements! You can also report issues or open pull requests.

## License

This project is licensed under the MIT License.
