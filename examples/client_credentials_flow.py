from spotipy_twisted.oauth2 import SpotifyClientCredentials
import spotipy_twisted
import pprint

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy_twisted.Spotify(client_credentials_manager=client_credentials_manager)

search_str = 'Muse'
result = sp.search(search_str)
pprint.pprint(result)
