#! python3
# Prints the current weather for a location from the command line.

import json
import requests
import sys

APPID = 'Your_AppID_Here'

# Compute location from command line arguments
if len(sys.argv) < 2:
    print('Usage: quickweather.py city_name, 2-letter_country_code')
    sys.exit()
location = ' '.join(sys.argv[1:])
# Download the JSON data from openweathermap.org's API
url = 'http://api.openweathermap.org/data/2.5/weather?q=%s&APPID=%s&units=metric' % (
    location, APPID)
response = requests.get(url)
response.raise_for_status()

# Load JSON data into Python variable.
weatherData = json.loads(response.text)

# Uncomment to see the raw JSON text:
# print(response.text)
coord = weatherData['coord']
coord['lon']
print(f'longitude of {location} is {coord["lon"]}')
print(f'latitude of {location} is {coord["lat"]}')
w = weatherData['weather']
w[0]["description"]
main = weatherData['main']
print(f'Current weather in {location}:\n'
      f'{w[0]["main"]}-{w[0]["description"]}, '
      f'temperature is {main["temp"]}\N{DEGREE SIGN}C, and feels like {main["feels_like"]}\N{DEGREE SIGN}C')
