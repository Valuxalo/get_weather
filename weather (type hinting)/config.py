USE_ROUNDED_COORDS = False
OPENWEATHER_API = '56f96e1797aba38fcb8f00b318c45d96'

OPENWEATHER_URL = (
    "https://ru.api.openweathermap.org/data/2.5/weather?"
    "lat={latitude}&lon={longitude}&"
    "appid=" + OPENWEATHER_API + "&lang=ru"
    "&units=metric"
)

print(OPENWEATHER_URL)