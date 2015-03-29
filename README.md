# Spayify
This is a little utility that is designed to take a playlist, from Spotify, using the API and determining how much it would cost to buy this playlist. This will give you an idea whether it is worth paying for the subscription or just buying the singles.
## Supports
### Playlist Sources
* Spotify

### MP3 Sources
* 7Digital

## Usage
### Installation
    python setup.py install

### Get API Access
#### Spotify
1. You need a Spotify API access
1. Get your Client ID.
1. Using the `spayify.source.spotify.SourceAuth` request a short term access token. This token lasts an hour, which should be plenty of time. You can use whatever `redirect_url` you want as long as it is valid.
1. The request object will give you a URL you can use in your browser and once you have followed that process your browser will be dumped at your `redirect_url` with the access token in the URL.

#### 7digital
1. Sign up with the 7digital developer service. They will e-mail you an access code.

### The playlist
1. It is possible to use the `spayify.source.spotify.Source.get_playlists` to find your users playlists ids. Your `user_id` is your username.

### Getting the value of your playlist
1. Using `spayify.spayify.Lookup` create the object with your API keys/tokens.
1. Run `run` on that object with your spotify username and the paylist id. This will iterate over your playlist and add your values to a 7digital basket and give you the end price.

## Future
* YouTube playlist as Playlist source
* Google Play as MP3 Source
* Amazon MP3 as MP3 Source
