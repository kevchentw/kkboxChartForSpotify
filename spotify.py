import spotipy
from settings import settings
import spotipy.util as util
from time import sleep

class Spotify:
    def __init__(self):
        self.spotify = spotipy.Spotify()
        self.tokens = {}
        self.username = settings['username']

    def get_spotify(self, scope):
        s = self.tokens.get(scope)
        if s:
            return s
        else:
            return self.get_token(scope)

    def get_token(self, scope):
        token = util.prompt_for_user_token(self.username, scope)
        if token:
            try:
                s = self.tokens['scope'] = spotipy.Spotify(auth=token)
                return s
            except:
                print("spotify api error, sleep 5s...")
                sleep(5)
                return get_token(scope)
        else:
            return None

    def add_tracks(self, tracks, playlist):
        scope = 'playlist-modify-public playlist-modify-private'
        s = self.get_spotify(scope)
        try:
            r = s.user_playlist_add_tracks(self.username, playlist, tracks)
        except:
            print("spotify api error, sleep 5s...")
            sleep(5)
            r = self.add_tracks(tracks, playlist)

    def removes_tracks(self, tracks, playlist):
        scope = 'playlist-modify-public playlist-modify-private'
        s = self.get_spotify(scope)
        try:
            r = s.user_playlist_remove_all_occurrences_of_tracks(self.username, playlist, tracks)
        except:
            print("spotify api error, sleep 5s...")
            sleep(5)
            r = self.removes_tracks(tracks, playlist)


    def search_track(self, title, artist):
        q = 'artist:' + artist + " track:" + title
        print(q)
        try:
            results = self.spotify.search(q=q, type='track')
        except:
            print("spotify api error, sleep 5s...")
            sleep(5)
            self.search_track(title, artist)
        tracks = results['tracks']['items']
        if len(tracks) > 0:
            return tracks[0]
        else:
            return None

    def search_tracks(self, data):
        tracks = []
        for i in data:
            track = self.search_track(i['title'], i['artist'])
            if track:
                tracks.append(track['uri'])
        return tracks

    def get_playlist_tracks(self, playlist):
        scope = 'playlist-modify-public playlist-modify-private'
        s = self.get_spotify(scope)
        try:
            p = s.user_playlist_tracks(self.username, playlist, "items.track.id")
        except:
            print("spotify api error, sleep 5s...")
            sleep(5)
            r = self.get_playlist_tracks(playlist)
        tracks = []
        for i in p['items']:
            tracks.append(i['track']['id'])
        return tracks

