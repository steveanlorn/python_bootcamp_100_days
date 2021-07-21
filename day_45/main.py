from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.detik.com/indeks')
response.raise_for_status()
html_doc = response.text

soup = BeautifulSoup(html_doc, 'html.parser')

articles = soup.select('#indeks-container article h3 > a')
for article in articles:
    print(article.text)
    print(article['href'])
    print("------\n")
