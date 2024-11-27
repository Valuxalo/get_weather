from weather_api_service import Weather

def format_weather(weather: Weather) -> str:
    return (f"{weather.city}, температура {weather.temperature}°C\n"
            f"{weather.weather_type.value}, {weather.weather_descr}\n"
            f"Восход: {weather.sunrise}\n"
            f"Закат:  {weather.sunset}")