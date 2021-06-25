import requests
import datetime

API_HOST = "https://www.alphavantage.co/query"


class Stock:
    def __init__(self, key: str, stock_symbol: str):
        self.key = key
        self.stock_symbol = stock_symbol
        self.daily_stock = self.get_stock_daily()

    def get_stock_daily(self) -> {}:
        param = {
            "function": "TIME_SERIES_DAILY",
            "symbol": self.stock_symbol,
            "interval": "60min",
            "apikey": self.key,
        }

        response = requests.get(API_HOST, params=param)
        response.raise_for_status()
        response_body = response.json()["Time Series (Daily)"]

        stock_data = {}
        for r in response_body:
            dates = r.split(sep="-")
            year = int(dates[0])
            month = int(dates[1])
            day = int(dates[2])

            stock_data[datetime.date(year, month, day)] = {
                "open": float(response_body[r]["1. open"]),
                "high": float(response_body[r]["2. high"]),
                "low": float(response_body[r]["3. low"]),
                "close": float(response_body[r]["4. close"]),
                "volume": int(response_body[r]["5. volume"]),
            }

        self.daily_stock = stock_data

        return stock_data

    def stock_dif(self, start: datetime.date, end: datetime.date) -> float:
        if start not in self.daily_stock:
            raise AttributeError(Exception(start))

        if end not in self.daily_stock:
            raise AttributeError(Exception(end))

        new_value = self.daily_stock[end]["close"]
        old_value = self.daily_stock[start]["close"]
        difference = ((new_value - old_value) / ((new_value + old_value) / 2)) * 100
        return difference
