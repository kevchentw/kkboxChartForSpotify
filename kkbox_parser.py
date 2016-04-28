import requests
from bs4 import BeautifulSoup

test_url = "https://www.kkbox.com/tw/tc/charts/overall_newrelease-daily-song-latest.html"


def text_cleanup(s):
    return s.split("-")[0].split("(")[0].split("【")[0].split("<")[0].strip()


def get_chart(url):
    print("Fetching KKBOX WEB")
    r = requests.get(url).text
    print("Start Parsing KKBOX Chart")
    soup = BeautifulSoup(r)
    items = soup.find_all("div", {"class": "item"})
    data = []
    for idx, item in enumerate(items):
        d = {}
        d['title'] = text_cleanup(item.find("h4").text)
        d['artist'] = text_cleanup(item.find("h5").text)
        data.append(d)
    print("DONE")
    print(data)
    return data

