# Get hourly weather prediction for next 12 hours
# If there is chance to rain, send SMS

import requests
from twilio.rest import Client
import datetime
from dateutil import tz
import os

# OWM_KEY='xxx' TWILLIO_SID='xxx' TWILLIO_TOKEN='xxx' PHONE_FROM='+62xxx' PHONE_TO='+62xxx' python3 main.py

WEATHER_HOST = "https://api.openweathermap.org/data/2.5/onecall"

OWM_KEY = os.environ.get("OWM_KEY")
if OWM_KEY == "":
    raise Exception("Required OWM_KEY env variable")

TWILLIO_SID = os.environ.get("TWILLIO_SID")
if TWILLIO_SID == "":
    raise Exception("Required TWILLIO_SID env variable")

TWILLIO_TOKEN = os.environ.get("TWILLIO_TOKEN")
if TWILLIO_TOKEN == "":
    raise Exception("Required TWILLIO_TOKEN env variable")

# We can also add phone number validation
PHONE_FROM = os.environ.get("PHONE_FROM")
if PHONE_FROM == "":
    raise Exception("Required PHONE_FROM env variable")

# Prefer to use flag as this can change between execution.
PHONE_TO = os.environ.get("PHONE_TO")
if PHONE_TO == "":
    raise Exception("Required PHONE_TO env variable")

weather_param = {
    "lat": -6.917464,
    "lon": 107.619125,
    "exclude": "current,minutely,daily,alerts",
    "units": "metric",
    "appid": OWM_KEY,
}

response = requests.get(WEATHER_HOST, params=weather_param)
response.raise_for_status()
response_body = response.json()

seven_hours_prediction = response_body["hourly"][:12]

today_is_raining = False

rain_schedule = []

for prediction in seven_hours_prediction:
    # main weather condition
    weather = prediction["weather"][0]

    # it's raining, do something
    # ref: https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2
    if 200 <= weather["id"] < 600:
        today_is_raining = True

        from_zone = tz.gettz('UTC')
        to_zone = tz.gettz('Asia/Jakarta')

        timestamp = datetime.datetime.fromtimestamp(prediction['dt'])
        timestamp.replace(tzinfo=from_zone)
        local_time = timestamp.astimezone(to_zone)

        rain_schedule.append(
            f"{local_time.strftime('%Y-%m-%d %H:%M:%S')} - {weather['description']}")

if today_is_raining:
    # send notification using SMS via Twilio
    client = Client(TWILLIO_SID, TWILLIO_TOKEN)

    rain_schedules = '\n'.join(rain_schedule)

    message_body = f"""TODAY IS GOING TO RAIN!
Rain schedule:
{rain_schedules}

Don't forget to bring umbrella!
    """

    message = client.messages \
        .create(
            body=message_body,
            from_=PHONE_FROM,
            to=PHONE_TO,
        )

    print(f"""
Sending SMS from {PHONE_FROM}
To {PHONE_TO}
Status {message.status}
Message:
{message_body}
    """)
