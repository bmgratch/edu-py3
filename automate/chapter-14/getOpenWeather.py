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

# Load JSON data into a python variable
weatherData = json.loads(response.text)

# Print weather descriptions
w = weatherData['list']
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
