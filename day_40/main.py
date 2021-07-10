from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
import notification_manager

import os

SHEETY_AUTH_USERNAME = os.environ.get("SHEETY_AUTH_USERNAME")
SHEETY_AUTH_PASSWORD = os.environ.get("SHEETY_AUTH_PASSWORD")
data_manager = DataManager(SHEETY_AUTH_USERNAME, SHEETY_AUTH_PASSWORD)


TEQUILA_KEY = os.environ.get("TEQUILA_KEY")
flight_search = FlightSearch(TEQUILA_KEY)

sheet_data = data_manager.get_destination_data()

ORIGIN_CITY_IATA = "JKT"

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

users = data_manager.get_customer_emails()

message = ""

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

    if flight is None:
        continue

    if flight.price < destination["lowestPrice"] or destination["lowestPrice"] == 0:
        message += f"Rp{flight.price} dari {flight.origin_city}-{flight.origin_airport} ke {flight.destination_city}-{flight.destination_airport}, dari tanggal {flight.out_date} ke {flight.return_date}."

        if flight.stop_overs > 0:
            message += f"\nPenerbangan memiliki {flight.stop_overs} pemberhentian, via {flight.via_city}."

        message += f"\nhttps://www.google.co.uk/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}.{flight.out_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}\n\n"

if len(message) > 0:
    notification_manager.send_emails(users, message)
