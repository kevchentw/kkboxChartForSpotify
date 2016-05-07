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


### LICENSE
MIT
