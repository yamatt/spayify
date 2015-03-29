from source.spotify import Source
from mp3s.sevendigital import Mp3s

class Track(object):
    ARTIST = None
    TRACK = None

class Lookup(object):
    def __init__(self, source_token, mp3_token):
        self.source = Source(source_token)
        self.mp3 = Mp3s(mp3_token)
        
    def run(self, user_id, playlist_id):
        tracks = self.source.get_all_playlist_tracks(user_id, playlist_id)
        basket_id = self.mp3.create_basket()
        print u"Basked ID:", basket_id
        for track in tracks:
            release_id = self.mp3.get_track(track['track']['artists'][0]['name'], track['track']['name'])
            if release_id:
                r = self.mp3.add_to_basket(basket_id, release_id)
                print u"Added {0} - {1} ({2})".format(track['track']['artists'][0]['name'], track['track']['name'], release_id)
            else:
                print u"Could not find {0} - {1}".format(track['track']['artists'][0]['name'], track['track']['name'])
        print "Basked Price:", self.mp3.get_basket_price(basket_id)
