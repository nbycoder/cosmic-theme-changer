from astral import LocationInfo
import pytz
from datetime import datetime
from astral.sun import sun

tz = pytz.timezone('Europe/Lisbon') # REPLACE WITH YOUR OWN TIME
date = datetime.now()

today = date.replace(tzinfo=tz)

# city = LocationInfo("city", "country", "timezone", latitude, longitude)
city = LocationInfo("Lisbon", "Portugal", "Europe/Lisbon", 41.44, -8.29)
s = sun(city.observer, date=today, tzinfo=tz)
sunset = s["sunset"] # alternatively you can also use sunrise, dawn & dusk here
