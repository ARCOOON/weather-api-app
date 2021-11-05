import time
import datetime as dt


def getTemp(weather_data):
    return weather_data["list"][0]['main']['temp']


def getDescription(weather_data):
    return weather_data["list"][0]['weather'][0]['description']


def getIcon(weather_data):
    return weather_data["list"][0]['weather'][0]['icon']


def getIconLink(weather_data, size=2):
    iconData = weather_data["list"][0]['weather'][0]['icon']
    iconLink = (f"http://openweathermap.org/img/wn/{iconData}@{size}x.png")
    return iconLink


def getWeather(weather_data):
    return weather_data["list"][0]['weather'][0]['main']


def getWindDegrees(weather_data):
    return weather_data["list"][0]['wind']['deg']


class util:
    class time:
        def __init__(self, timeObject):
            self.timeObject = timeObject.datetime.now()

        def hours(self):
            return self.timeObject.strftime('%H')

        def minutes(self):
            return self.timeObject.strftime('%M')

        def seconds(self):
            return self.timeObject.strftime('%S')
        
        def getSet(self):
            h = self.hours()
            m = self.minutes()
            return str(f'{h} : {m}')

    def ui(self):
        return self

# https://api.openweathermap.org/data/2.5/forecast?q=Salzburg,5020&appid=5345258a13b1617455dc98c171bf0393