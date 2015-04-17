# shows artist info for a URN or URL

import spotipy_twisted
import sys
import pprint

if len(sys.argv) > 1:
    urn = sys.argv[1]
else:
    urn = 'spotify:artist:3jOstUTkEu2JkjvRdBA5Gu'

sp = spotipy_twisted.Spotify()
response = sp.artist_top_tracks(urn)

for track in response['tracks']:
    print track['name']
