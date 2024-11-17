from datetime import datetime
from typing import Literal, NamedTuple

from urllib.request import urlopen
from urllib.error import URLError

from get_gps import Coordinates
from enum import Enum
import ssl
import json
from json import JSONDecodeError
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
        return urlopen(url).read()
    except URLError:
        raise ApiServiceError

def _parse_openweather_response(openweather_response:str) -> Weather:
    try:
        opeweather_dict = json.load(openweather_response)
    except JSONDecodeError:
        raise ApiServiceError
    return Weather(
        temperature=_parse_temperature(opeweather_dict),
        weather_type=_parse_weather_type(opeweather_dict),
        sunrise=_parse_sun_time(opeweather_dict, 'sunrise'),
        sunset=_parse_sun_time(opeweather_dict, 'sunset'),
        city=_parse_city(opeweather_dict)
        )
    

def _parse_temperature(opeweather_dict:dict) -> Celsius:
    return round(opeweather_dict['main']['temp'])

def _parse_weather_type(opeweather_dict:dict) -> WeatherType:
    try:
        weather_type_id = str(opeweather_dict['weather'][0]['id'])
    except (IndexError, KeyError):
        raise ApiServiceError
    weather_types = {
        '2': WeatherType.Thunderstorm,
        '3': WeatherType.Drizzle,
        '5': WeatherType.Rain,
        '6': WeatherType.Snow,
        '7': WeatherType.Atmosphere,
        '800': WeatherType.Clear,
        '80': WeatherType.Clouds
    }
    for _id, _weather_type in weather_types.items():
        if weather_type_id.startswith(_id):
            return _weather_type

def _parse_sun_time(
        opeweather_dict:dict,
        time: Literal["sunrise","sunset"]) -> datetime:
    return datetime.fromtimestamp(opeweather_dict['sys'][time]).strftime('%Y-%m-%d %H:%M:%S')

def _parse_city(opeweather_dict:dict) -> str:
    return opeweather_dict['name']