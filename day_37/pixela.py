import datetime
import requests
import random
import re

HOST_NAME = "https://pixe.la"
VERSION = "1"

end_points = {
    "user": "users",
    "create_graph": "users/<username>/graphs",
    "graph": "users/<username>/graphs/<graphID>",
    "increment": "users/<username>/graphs/<graphID>/increment"
}


def get_endpoint(end_point: str, username="", graph_id="") -> str:
    if end_point not in end_points:
        raise ValueError(f"end_point should be in {end_points.keys()}")
    else:

        ep = end_points[end_point]
        ep = ep.replace("<username>", username)
        ep = ep.replace("<graphID>", graph_id)

        return f"{HOST_NAME}/v{VERSION}/{ep}"


token_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

colors = {
    "green": "shibafu",
    "red": "momiji",
    "blue": "sora",
    "yellow": "ichou",
    "purple": "ajisai",
    "black": "kuro",
}

types = {
    "float": "float",
    "int": "int",
}


def generate_token() -> str:
    token = ""
    for i in range(128):
        token += random.choice(token_chars)
    return token


def is_valid_graph_id(graph_id: str) -> bool:
    pattern = re.compile("^[a-z][a-z0-9-]{1,16}$")
    if pattern.search(graph_id):
        return True
    else:
        return False


def is_valid_username(user_name: str) -> bool:
    pattern = re.compile("^[a-z][a-z0-9-]{1,32}$")

    if pattern.search(user_name):
        return True
    else:
        return False


def create_user(user_name: str) -> str:
    url = get_endpoint("user")
    token = generate_token()

    if not is_valid_username(user_name):
        raise ValueError("Invalid user name. Must comply with rule: '[a-z][a-z0-9-]{1,32}'")

    param = {
        "token": token,
        "username": user_name,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }

    response = requests.post(url=url, json=param)
    response.raise_for_status()

    return token


class Pixela:
    def __init__(self, user_name: str, token=""):
        """Initialize Pixela.
        If token is empty then new user will be created.
        Else will assume user_name has been created.
        """

        if token == "":
            token = create_user(user_name=user_name)

        self.token = token
        self.username = user_name

    def create_graph(self, graph_id: str, name: str, unit: str, quantity_type: str, color: str):
        url = get_endpoint("create_graph", username=self.username)

        if quantity_type not in types:
            raise ValueError(f"quantity_type should be in {types.keys()}")

        if color not in colors:
            raise ValueError(f"color should be in {colors.keys()}")

        param = {
            "id": graph_id,
            "name": name,
            "unit": unit,
            "type": types[quantity_type],
            "color": colors[color],
            "timezone": "Asia/Jakarta",
        }

        header = {
            "X-USER-TOKEN": self.token
        }

        response = requests.post(url=url, json=param, headers=header)
        response.raise_for_status()

    def create_pixel(self, graph_id: str, date: datetime.date, quantity: str):
        url = get_endpoint("graph", username=self.username, graph_id=graph_id)

        param = {
            "date": date.strftime("%Y%m%d"),
            "quantity": quantity,
        }

        header = {
            "X-USER-TOKEN": self.token
        }

        response = requests.post(url=url, json=param, headers=header)
        response.raise_for_status()

    def delete_graph(self, graph_id: str):
        url = get_endpoint("graph", username=self.username, graph_id=graph_id)

        header = {
            "X-USER-TOKEN": self.token
        }

        response = requests.delete(url=url, headers=header)
        response.raise_for_status()

    def increment_pixel(self, graph_id: str):
        url = get_endpoint("increment", username=self.username, graph_id=graph_id)

        header = {
            "X-USER-TOKEN": self.token,
            "Content-Length": 0,
        }

        response = requests.put(url=url, headers=header)
        response.raise_for_status()

    def get_graph_url(self, graph_id: str) -> str:
        url = get_endpoint("graph", username=self.username, graph_id=graph_id) + ".html"
        return url
