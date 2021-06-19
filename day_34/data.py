import requests

parameter = {
    "amount": 10,
    "type": "boolean",
}

response = requests.get("https://opentdb.com/api.php", params=parameter, timeout=3)
response.raise_for_status()
question_data = response.json()["results"]
