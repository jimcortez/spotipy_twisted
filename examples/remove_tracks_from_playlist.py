
# Adds tracks to a playlist

import pprint
import sys

import spotipy_twisted
import spotipy_twisted.util as util

if len(sys.argv) > 3:
    username = sys.argv[1]
    playlist_id = sys.argv[2]
    track_ids = sys.argv[3:]
else:
    print "Usage: %s username playlist_id track_id ..." % (sys.argv[0],)
    sys.exit()

scope = 'playlist-modify-public'
token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy_twisted.Spotify(auth=token)
    sp.trace = False
    results = sp.user_playlist_remove_all_occurrences_of_tracks(username, playlist_id, track_ids)
    pprint.pprint(results)
else:
    print "Can't get token for", username
