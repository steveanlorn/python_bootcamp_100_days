import datetime
from stock import Stock
from news import News
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# NEWSAPIKEY='xxx' ALPHAVANTAGEKEY='xxx' python3 main.py
ALPHAVANTAGE_KEY = os.environ.get("ALPHAVANTAGEKEY")
NEWSAPI_KEY = os.environ.get("NEWSAPIKEY")

stock = Stock(ALPHAVANTAGE_KEY, STOCK)

today = datetime.datetime.now()
start = today - datetime.timedelta(days=2)
end = today - datetime.timedelta(days=1)

diff = stock.stock_dif(start=start.date(), end=end.date())

indicator = "🔻"
if diff > 0:
    indicator = "🔺"

if abs(diff) > 1:
    news = News(NEWSAPI_KEY)
    articles = news.get_news(q=COMPANY_NAME, start=start.date(), end=end.date())

    size = 3
    if len(articles) < 3:
        size = len(articles)

    articles = articles[:size]

    # Can follow day 35 for sending email or SMS
    print(f"{STOCK}: {indicator}{diff}%")
    for article in articles:
        print("------")
        print(f"Headline: {article['title']}")

        # may contain HTML tag, need to clean it up
        print(f"Brief: {article['description']}")
        print(f"URL: {article['url']}")
