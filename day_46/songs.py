import datetime
from bs4 import BeautifulSoup
import requests

URL = "https://www.billboard.com/charts/hot-100/{year}-{month}-{day}"


def get_top_100(date: datetime.date) -> list[dict[str, str]]:
    response = requests.get(URL.format(year=date.year, month=date.month, day=date.day))
    response.raise_for_status()

    html_doc = response.text

    soup = BeautifulSoup(html_doc, 'html.parser')
    songs = soup.select('.chart-list__element')

    songs_dic = []
    for song in songs:
        title = song.find(class_='chart-element__information__song').text
        artist = song.find(class_='chart-element__information__artist').text
        songs_dic.append({
            'title': title,
            'artist': artist,
        })

    return songs_dic
