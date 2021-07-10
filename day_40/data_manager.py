# This class is responsible for talking to the Google Sheet.

import requests
from requests.auth import HTTPBasicAuth

SHEETY_USERS = "https://api.sheety.co/db2fcbf5b488ac4008fe26ad5f4bbab1/flightDeals/users"
SHEETY_PRICES = "https://api.sheety.co/db2fcbf5b488ac4008fe26ad5f4bbab1/flightDeals/prices"


class DataManager:
    def __init__(self, username: str, password: str):
        self.auth = HTTPBasicAuth(username, password)
        self.destination_data = {}
        self.customer_data = {}

    def get_destination_data(self) -> dict:
        response = requests.get(url=SHEETY_PRICES, auth=self.auth)
        response.raise_for_status()
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }

            response = requests.put(
                url=f"{SHEETY_PRICES}/{city['id']}",
                json=new_data,
                auth=self.auth,
            )

            response.raise_for_status()

    def get_customer_emails(self):
        customers_endpoint = SHEETY_USERS
        response = requests.get(url=customers_endpoint, auth=self.auth)
        response.raise_for_status()
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
