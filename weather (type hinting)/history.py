from datetime import datetime
from pathlib import Path

from weather_api_service import Weather
from weather_formatter import format_weather

class WeatherStorage:
    """Интерфейс для каждого хранилища"""
    def save(self, weather: Weather) -> None:
        raise NotImplementedError #поднимется, если нереализован метод save у дочернего класса
    
class PlainFileWeatherStorage(WeatherStorage):
    def __init__(self, file: Path):
        self._file = file

    def save(self, weather: Weather) -> None:
        now = datetime.now()
        format = format_weather(weather)
        with open(self._file, "a") as f:
            f.write(f"{now}\n{format}\n\n")

def save_weather(weather: Weather, storage: WeatherStorage):
    storage.save(weather)