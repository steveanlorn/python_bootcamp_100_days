# This class is responsible for talking to the Google Sheet.

import requests
from requests.auth import HTTPBasicAuth


class DataManager:
    def __init__(self, end_point: str, username: str, password: str):
        self.end_point = end_point
        self.auth = HTTPBasicAuth(username, password)
        self.destination_data = {}

    def get_destination_data(self) -> dict:
        response = requests.get(url=self.end_point, auth=self.auth)
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
                url=f"{self.end_point}/{city['id']}",
                json=new_data,
                auth=self.auth,
            )

            print(response.text)
