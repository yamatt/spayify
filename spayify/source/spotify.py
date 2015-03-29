import requests
from uuid import uuid4
from urlparse import urljoin

class SourceAuth(object):
    BASE_URL = 'https://accounts.spotify.com/authorize'
    SCOPE = "user-read-private user-read-email playlist-read-private"
    
    def __init__(self, client_id, redirect_url):
        self.client_id = client_id
        self.redirect_url = redirect_url
        self.scope = self.SCOPE
        
    def generate_state(self):
        return uuid4().hex
    
    def create_auth_querystring(self):
        return {
            "response_type": "token",
            "client_id": self.client_id,
            "scope": self.scope,
            "redirect_uri": self.redirect_url,
            "state": self.generate_state()
        }
        
    def get_auth_page(self):
        return requests.get(self.BASE_URL, params=self.create_auth_querystring())

class Source(object):
    BASE_URL = "https://api.spotify.com/v1/"
    def __init__(self, access_token):
        self.token = access_token
        
    def create_headers(self):
        return {
            'Authorization': 'Bearer ' + self.token
        }
        
    def get_json(self, url, params={}):
        response = requests.get(url, headers=self.create_headers(), params=params)
        return response.json()
        
    def get_user_id(self):
        url = urljoin(self.BASE_URL, "me")
        return self.get_json(url).get("id")
        
    def get_playlists(self, user_id):
        url = urljoin(self.BASE_URL, "users/{0}/playlists".format(user_id))
        return self.get_json(url)
        
    def get_playlist_tracks(self, user_id, playlist_id, params={}):
        url = urljoin(self.BASE_URL, "users/{0}/playlists/{1}/tracks".format(user_id, playlist_id))
        return self.get_json(url, params)
        
    def get_all_playlist_tracks(self, user_id, playlist_id):
        playlist = self.get_playlist_tracks(user_id, playlist_id)
        tracks = playlist['items']
        while len(tracks) < playlist['total']:
            params = {
                "offset": len(tracks)
            }
            playlist = self.get_playlist_tracks(user_id, playlist_id, params)
            tracks += playlist['items']
        return tracks
        
