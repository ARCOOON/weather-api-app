from utils import *
from weather import Weather, WeatherData

print(WeatherData().init("Salzburg", "5020", "5345258a13b1617455dc98c171bf0393").get())