import requests
import json

class Weather:
    def __init__(self, weather_object):
        self.weather_data = []

class WeatherData:
    def __init__(self):
        return self

    def init(self, city, zipcode, appid):
        self.city = city
        self.zipcode = zipcode
        self.appid = appid

        return self
    
    def get():
        url = f"https://api.openweathermap.org/data/2.5/forecast?q={self.city},{self.zipcode}&appid={self.appid}"
        response = requests.get(url)
        data = json.loads(response.text)

        return data
