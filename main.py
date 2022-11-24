# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import datetime as dt
import requests as rq
import json as js


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def kelving_to_celcius_fahrenhite(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with open('secrets.json') as secret_file:
        all_secrets = js.load(secret_file)


    print_hi('PyCharm')
    BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'
    API_KEY = all_secrets['api_key']
    CITY = 'Plano'



    url = BASE_URL + 'appid=' + API_KEY + '&q=' + CITY
    print(url)
    response = rq.get(url).json()
    print(response)
    temp_kelvin = response['main']['temp']
    celsius, fahrenheit = kelving_to_celcius_fahrenhite(temp_kelvin)
    feels_like_kelvin = response['main']['feels_like']
    feels_like_celsius, feels_like_fahrenheit = kelving_to_celcius_fahrenhite(feels_like_kelvin)
    wind_speed = response['wind']['speed']
    humidity = response['main']['humidity']
    description = response['weather'][0]['description']
    sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
    sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])


    print(f'Temperature in {CITY}: {celsius:.2f}C or {fahrenheit:.2f}F')
    print(f'Temperature in {CITY} feels like: {feels_like_celsius:.2f}C or {feels_like_fahrenheit:.2f}F')
    print(f'Humidity in {CITY}: {humidity}')
    print(f'Wind Speed in {CITY}: {wind_speed}m/s')
    print(f"General Weather in {CITY}: {description}")
    print(f"Sun Rises in {CITY}: {sunrise_time} local time")
    print(f"Sun Set in {CITY}: {sunset_time} local time")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
