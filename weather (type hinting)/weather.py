# !/usr/bin/env python3.13
from pathlib import Path
from get_gps import get_coordinate
from weather_api_service import get_weather
from weather_formatter import format_weather
from exceptions import ApiServiceError, CantGetCoordinates
from history import save_weather, PlainFileWeatherStorage
def main():
    try:
        coordinates = get_coordinate()
    except CantGetCoordinates:
        print("Не удалось получить GPS-координаты")
        exit(1)
    try:
        weather = get_weather(coordinates)
    except ApiServiceError:
        print(f"Не удалось получить погоду по координтам {coordinates}")
        exit(1)
    print(format_weather(weather))
    save_weather(weather, 
                 PlainFileWeatherStorage(Path.cwd() / "history.txt"))

if __name__ == "__main__":
    main()

