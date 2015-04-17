# shows track info for a URN or URL

import spotipy_twisted
import sys
import pprint

if len(sys.argv) > 1:
    urn = sys.argv[1]
else:
    urn = 'spotify:track:0Svkvt5I79wficMFgaqEQJ'

sp = spotipy_twisted.Spotify()
track = sp.track(urn)
pprint.pprint(track)
