
# Add tracks to 'Your Collection' of saved tracks

import pprint
import sys

import spotipy_twisted
import spotipy_twisted.util as util

scope = 'user-library-modify'

if len(sys.argv) > 2:
    username = sys.argv[1]
    tids = sys.argv[2:]
else:
    print "Usage: %s username track-id ..." % (sys.argv[0],)
    sys.exit()

token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy_twisted.Spotify(auth=token)
    sp.trace = False
    results = sp.current_user_saved_tracks_add(tracks=tids)
    pprint.pprint(results)
else:
    print "Can't get token for", username
