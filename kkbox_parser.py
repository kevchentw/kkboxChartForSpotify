import requests
from bs4 import BeautifulSoup
import re

test_url = "https://www.kkbox.com/tw/tc/charts/overall_newrelease-daily-song-latest.html"


def text_cleanup(s):
    text = s.split("-")[0].split("(")[0].split("【")[0].split("<")[0].strip()
    text = text.replace("+", " ")
    text = text.replace(",", " ")
    return text


def get_chart(url):
    r = requests.get(url).text
    soup = BeautifulSoup(r)
    items = soup.find_all("div", {"class": "item"})
    data = []
    for idx, item in enumerate(items):
        d = {}
        d['title'] = text_cleanup(item.find("h4").text)
        d['artist'] = text_cleanup(item.find("h5").text)
        data.append(d)
    return data

