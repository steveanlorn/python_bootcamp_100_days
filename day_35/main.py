# Get hourly weather prediction for next 12 hours
# Weather check will start run at 7AM
# Will check if there is chance to rain from 7AM - 7PM

import requests
import smtplib
import datetime
from dateutil import tz
import os

WEATHER_HOST = "https://api.openweathermap.org/data/2.5/onecall"
OWM_KEY = os.environ.get("OWM_KEY")

EMAIL = ""
EMAIL_PASSWORD = os.environ.get("EMAIL_PWD")

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

        rain_schedule.append(f"{local_time.strftime('%Y-%m-%d %H:%M:%S')} - {weather['main']} - {weather['description']}")

if today_is_raining:

    # send notification using SMS via Twilio
    # unfortunately my phone number could not receiver Twilio's confirmation SMS somehow :(
    # so lets send notification with email instead.

    email_connection = smtplib.SMTP("smtp.gmail.com")
    email_connection.starttls()
    email_connection.login(user=EMAIL, password=EMAIL_PASSWORD)

    rain_schedules = '\n'.join(rain_schedule)

    message_body = f"""
Rain schedule:
{rain_schedules}

Don't forget to bring umbrella!
    """

    email_connection.sendmail(
        from_addr=EMAIL,
        to_addrs=EMAIL,
        msg=f"Subject:TODAY IS GOING TO RAIN!\n\n{message_body}")

    email_connection.close()
