from datetime import datetime
from typing import NamedTuple

import urllib
from urllib.error import URLError

from get_gps import Coordinates
from enum import Enum
import ssl
from exceptions import ApiServiceError
from config import OPENWEATHER_URL
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
    openweather_response = _get_openweather_response(
        longitude=coordinates.longitude, latitude=coordinates.latitude)
    weather = _parse_openweather_response(openweather_response)
    return weather

def _get_openweather_response(longitude=float, latitude=float) -> str:
    ssl._create_default_https_context = ssl._create_unverified_context
    url = OPENWEATHER_URL.format(longitude=longitude, latitude=latitude)
    try:
        return urllib.request.urlopen(url).read()
    except URLError:
        raise ApiServiceError

def _parse_openweather_response(openweather_response:str) -> Weather:


