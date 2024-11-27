USE_ROUNDED_COORDS = True
OPENWEATHER_API = '56f96e1797aba38fcb8f00b318c45d96'

OPENWEATHER_URL = (
    "https://api.openweathermap.org/data/2.5/weather?"
    "lat={latitude}&lon={longitude}&"
    "appid=" + OPENWEATHER_API + "&lang=ru"
    "&units=metric"
)

OPENWEATHER_RU_URL = (
    "https://ru.api.openweathermap.org/data/2.5/weather?"
    "lat={latitude}&lon={longitude}&"
    "appid=" + OPENWEATHER_API + "&lang=ru"
    "&units=metric"
)