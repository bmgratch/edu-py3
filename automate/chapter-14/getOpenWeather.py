#! python3
# getOpenWeather.py - prints the weather for a location from command line.

APPID = 'YOUR_APPID_HERE'

import json, requests, sys

# Compute loaction from command line arguments.
if len(sys.argv) < 2:
    print('Usage: getOpenWeather.py city_name, 2-letter_country_code')
    sys.exit()
location = ''.join(sys.argv[1:])

# Download the JSON data from OpenWeatherMap.org's APO
url = 'https://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3&APPID=%s' % (location, APPID)
response = requests.get(url)
response.raise_for_status()
# Uncomment this to see the raw JSON text:
#print(reponse.text)

#TODO Load JSON data into a python variable
