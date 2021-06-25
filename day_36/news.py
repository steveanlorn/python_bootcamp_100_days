import requests
import datetime

API_HOST = "https://newsapi.org/v2/everything"


class News:
    def __init__(self, key: str):
        self.key = key

    def get_news(self, q: str, start: datetime.date, end: datetime.date):
        param = {
            "apiKey": self.key,
            "q": q,
            "from": start.strftime("%Y-%m-%d"),
            "to": end.strftime("%Y-%m-%d"),
            "sortBy": "relevancy",
        }

        response = requests.get(API_HOST, params=param)
        response.raise_for_status()
        response_body = response.json()

        articles_response = response_body["articles"]

        articles = []
        for article in articles_response:
            articles.append(
                {
                    "source": {
                        "id": article["source"]["id"],
                        "name": article["source"]["name"]
                    },
                    "author": article["author"],
                    "title": article["title"],
                    "description": article["description"],
                    "url": article["url"],
                    "urlToImage": article["urlToImage"],
                    "publishedAt": article["publishedAt"],
                    "content": article["content"],
                }
            )

        return articles
