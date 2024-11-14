from datetime import datetime
from typing import NamedTuple

from get_gps import Coordinates
from enum import Enum

Celsius = int

class WeatherType(Enum):
    Thunderstorm = 'Гроза'
    Drizzle = 'Изморось'
    Rain = 'Дождь'
    Snow = 'Снег'
    Atmosphere = 'Туман'
    Clear = 'Ясно'
    Clouds = 'Облачно'

class Weather(NamedTuple):
    temperature: Celsius
    weather_type: WeatherType
    sunrise: datetime
    sunset: datetime
    city: str

def get_weather(coordinates: Coordinates) -> Weather:
    pass

