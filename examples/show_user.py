
# shows artist info for a URN or URL

import spotipy_twisted
import sys
import pprint

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    username = 'plamere'

sp = spotipy_twisted.Spotify()
sp.trace = True
user = sp.user(username)
pprint.pprint(user)

