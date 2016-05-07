# KKBOX Chart for Spotify

### Usage

- Install Python 3
- Install Requirements
`pip3 install -r requirements.txt`
- Register your app at https://developer.spotify.com/my-applications/#!/applications   
- Setup settings.py

```
settings['username'] = ""
settings['client_id'] = ""
settings['client_secret'] = ""
settings['redirect_uri'] = ""
```

- Add your target job at ``jobs.txt``
```
playist_id KKBOX_Chart_URL
...
```

- Start Running ``python3 main.py``

### Want more music Charts?

Write your own chart web parser.
You should send a list of music's title & artist to `search_tracks(data)`, it will start search the track on Spotify API.

The Structure of the Data is
```
[
    {'title': '', 'artist': ''}, ............
]
```

### Where is the Spotify Playlist?

- KKBOX每日排行榜(中文)每日更新 https://open.spotify.com/user/11124349391/playlist/1uUeh9uyMkfolyQ5nWCNjm
- KKBOX每日排行榜(英文)每日更新 https://open.spotify.com/user/11124349391/playlist/6wkfdvtpEoAD40dk781gEo
- KKBOX每日排行榜(日語)每日更新 https://open.spotify.com/user/11124349391/playlist/1cu1cyGWCE1uYhuHrcxWaN
- KKBOX每日排行榜(台語)每日更新 https://open.spotify.com/user/11124349391/playlist/5QNJB8JsGoEONFFfsy5PIW
- KKBOX每日排行榜(韓語)每日更新 https://open.spotify.com/user/11124349391/playlist/28W2GcZukUNgiQqcArk31o
- KKBOX每日排行榜(粵語)每日更新 https://open.spotify.com/user/11124349391/playlist/6AJNRj4L85G5Ftninq2Bip
- KKBOX新歌排行(中文)每日更新 https://open.spotify.com/user/11124349391/playlist/4yBQStm0d3dhgSOdpuxXYy
- KKBOX新歌排行(英文)每日更新 https://open.spotify.com/user/11124349391/playlist/26aAy1mCRixJAFdEzTgVty
- KKBOX新歌排行(日語)每日更新 https://open.spotify.com/user/11124349391/playlist/3pXKUG5kVqNP6c2Zv4mCXU
- KKBOX新歌排行(粵語)每日更新 https://open.spotify.com/user/11124349391/playlist/7MY3duYPXXyfSbakOYUyO1
- KKBOX新歌排行(台語)每日更新 https://open.spotify.com/user/11124349391/playlist/0HJogJvuYxuZZXcEIulKd1
- KKBOX新歌排行(韓語)每日更新 https://open.spotify.com/user/11124349391/playlist/1ZJ0Hi1F5gYGPfUxVBt3MS

### LICENSE
MIT
