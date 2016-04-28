from spotify import Spotify
from kkbox_parser import get_chart, test_url

data = get_chart(test_url)

sp = Spotify()
f = open("jobs.txt", "r")
jobs = f.readlines()
for i in jobs:
    playlist, url = i.split(" ")
    data = get_chart(url)
    tracks = sp.search_tracks(data)
    old_tracks = sp.get_playlist_tracks(playlist)
    sp.removes_tracks(old_tracks, playlist)
    sp.add_tracks(tracks, playlist)
    sp.get_playlist_tracks(playlist)

