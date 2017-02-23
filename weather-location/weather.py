''' Getting the current weather outside for a location and response format http://openweathermap.org/current#data '''
import requests, json, sys

''' error if not enough arguments are given'''
if len(sys.argv) < 3:
    print('Usage: python weather.py city country_code')
    sys.exit()

''' define vars '''
city_name = ' '.join(sys.argv[1:2])
country_code = ' '.join(sys.argv[2])
response_format = 'json'
api_key = 'KEY_HERE'
url = 'http://api.openweathermap.org/data/2.5/weather?q=%s,%s&mode=%s&units=imperial&appid=%s' % (city_name, country_code, response_format, api_key)
response = requests.get(url)

''' Load the json into a list '''
weather_data = json.loads(response.text)

''' Get the dictionary info for temp, clouds and wind speed'''
current_temp = weather_data['main']['temp']
clouds = weather_data['weather'][0]['description']
wind_speed = weather_data['wind']['speed']

''' Print currents for location '''
print('Currently in %s it is %i with wind speeds of %i and %s. ' % (city_name, current_temp, wind_speed, clouds))




