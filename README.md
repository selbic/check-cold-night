# check-cold-night
Checks public weather data if temp in coming night will drop and warns me via my android phone

Uses Pushbullet for the push-msg on the phone and OpenWeather data API. 

Runs via Action at 9 UTC daily and sends push msg to my phone with temp of coming night (will be changed that it only sends the temp once it drops below -4 degrees Celsius). 

Time to get the plants into the garage!


***Nice:
GitHub Actions are used to run a Python skript
GitHub Secrets and environment variables are used in order to keep API Keys invisible

