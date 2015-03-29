import requests
from xml.etree import ElementTree
from urlparse import urljoin

class BaseSpayify(object):
    def create_url(self, url):
        return urljoin(self.BASE_URL, url)

class Mp3s(BaseSpayify):
    BASE_URL=u"http://api.7digital.com/1.2/"
    
    def __init__(self, key):
        self.key = key
    
    def search_artist_track(self, artist, track_name):
        return self.search(u"{0} {1}".format(artist, track_name))
        
    def search(self, query):
        url = self.create_url(u"track/search")
        params = {
            "q": query
        }
        return self.make_request(url, params=params)
        
    def setup_params(self):
        return {
            u"country": u"GB",
            u"oauth_consumer_key": self.key
        }
        
    def make_request(self, url, **kwargs):
        kwargs['params'] =  kwargs.get("params", {})
        kwargs['params'].update(self.setup_params())
        response = requests.get(url, **kwargs)
        return ElementTree.fromstring(response.content)
        
    def get_track(self, artist, track_name):
        tracks_xml = self.search_artist_track(artist, track_name)
        release = tracks_xml.find('./searchResults/searchResult/track/release')
        if release:
            return release.attrib['id']
        
    def create_basket(self):
        url = self.create_url(u"basket/create")
        response_xml = self.make_request(url)
        return response_xml.find("./basket").attrib['id']
        
    def add_to_basket(self, basket_id, release_id):
        url = self.create_url(u"basket/create")
        params = {
            u"basketId": basket_id,
            u"releaseId": release_id
        }
        return self.make_request(url, params=params)
        
    def get_basket_price(self, basket_id):
        url = self.create_url(u"basket")
        response_xml = self.make_request(url)
        return response_xml

