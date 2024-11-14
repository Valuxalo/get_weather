# !/usr/bin/env python3.13
from get_gps import get_coordinate
from weather_api_service import get_weather
from weather_formatter import format_weather

def main():
    coorfinates = get_coordinate()
    weather = get_weather(coordinates)
    print(format_weather(weather))

if __name__ == "__name__":
    main()

