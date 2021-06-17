import time
import requests
from datetime import datetime

MY_LAT = -6.917464
MY_LONG = 107.619125


def get_iss_coordinate():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    return iss_latitude, iss_longitude


def is_iss_above(iss_position):
    """Check if ISS position is above current location with a tolerance of 5 points"""
    lat = iss_position[0]
    long = iss_position[1]

    if lat - 5 <= MY_LAT <= lat + 5 and long - 5 <= MY_LONG <= long + 5:
        return True
    else:
        return False


def get_sunrise_sunset_hour():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise_hour = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_hour = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    return sunrise_hour, sunset_hour


sunrise, sunset = get_sunrise_sunset_hour()

while True:
    time_now = datetime.now()
    hour = time_now.utcnow().hour

    coordinate = get_iss_coordinate()
    if is_iss_above(coordinate) and sunset < hour < sunrise:
        pass
        # do something that can notify you, example sending an email

    time.sleep(60)
