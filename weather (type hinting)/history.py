from datetime import datetime
from pathlib import Path
from typing import TypedDict
import json

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

class HistoryRecord(TypedDict):
    date: str
    weather: str

class JSONFileWeatherStorage(WeatherStorage):
    def __init__(self, jsonfile: Path):
        self._jsonfile = jsonfile
        self._init_storage()

    def save(self, weather: Weather) -> None:
        history = self._read_history()
        history.append({
            "date": str(datetime.now()),
            "weather": format_weather(weather)
        })
        self._write(history)

    def _init_storage(self) -> None:            #инициализация JSON-файла, нужно записать []
        if not self._jsonfile.exists():
            self._jsonfile.write_text("[]")

    def _read_history(self) -> list[HistoryRecord]:
        with open(self._jsonfile, "r") as f:
            return json.load(f)
        
    def _write(self, history: list[HistoryRecord]) -> None:
        with open(self._jsonfile, "w") as f:
            json.dump(history, f, ensure_ascii=False, indent=4)

def save_weather(weather: Weather, storage: WeatherStorage):
    storage.save(weather)