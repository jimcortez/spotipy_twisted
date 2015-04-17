# shows tracks for the given artist

from __future__ import print_function
import spotipy_twisted
import sys
sp = spotipy_twisted.Spotify()

if len(sys.argv) > 1:
    artist_name = ' '.join(sys.argv[1:])
    results = sp.search(q=artist_name, limit=20)
    for i, t in enumerate(results['tracks']['items']):
        print(' ', i, t['name'])
