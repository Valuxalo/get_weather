import winsdk.windows.devices.geolocation as wdg
import asyncio
from typing import NamedTuple
from config import USE_ROUNDED_COORDS

class Coordinates(NamedTuple):
    latitude: float
    longitude: float

async def getCoords():
    locator = wdg.Geolocator()
    pos = await locator.get_geoposition_async()
    return [pos.coordinate.latitude, pos.coordinate.longitude]

def get_coordinate() -> Coordinates:  
    latitude = longitude = None
    latitude, longitude = asyncio.run(getCoords())
    #округление координат
    if USE_ROUNDED_COORDS:
        latitude, longitude = map(lambda c: round(c, 3), [latitude, longitude])
        
    return Coordinates(latitude=latitude, longitude=longitude)

# coordinate = get_coordinate()
# print(coordinate.latitude, coordinate.longitude)