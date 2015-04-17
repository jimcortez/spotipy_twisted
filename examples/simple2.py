
import spotipy_twisted


lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'

spotify = spotipy_twisted.Spotify()

results = spotify.artist_top_tracks(lz_uri)

for track in results['tracks'][:10]:
    print 'track    : ' + track['name']
    print 'audio    : ' + track['preview_url']
    print 'cover art: ' + track['album']['images'][0]['url']
    print
