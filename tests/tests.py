# -*- coding: latin-1 -*-
import spotipy_twisted
from twisted.trial import unittest
from spotipy_twisted.client import SpotifyException
from twisted.internet import defer


class TestSpotipy(unittest.TestCase):
    creep_urn = 'spotify:track:3HfB5hBU0dmBt8T0iCmH42'
    creep_id = '3HfB5hBU0dmBt8T0iCmH42'
    creep_url = 'http://open.spotify.com/track/3HfB5hBU0dmBt8T0iCmH42'
    el_scorcho_urn = 'spotify:track:0Svkvt5I79wficMFgaqEQJ'
    pinkerton_urn = 'spotify:album:04xe676vyiTeYNXw15o9jT'
    weezer_urn = 'spotify:artist:3jOstUTkEu2JkjvRdBA5Gu'
    pablo_honey_urn = 'spotify:album:6AZv3m27uyRxi8KyJSfUxL'
    radiohead_urn = 'spotify:artist:4Z8W4fKeB5YxbusRsdQVPb'

    bad_id = 'BAD_ID'

    def setUp(self):
        self.spotify = spotipy_twisted.Spotify()

    @defer.inlineCallbacks
    def test_artist_urn(self):
        artist = yield self.spotify.artist(self.radiohead_urn)
        defer.returnValue(self.assertTrue(artist['name'] == u'Radiohead'))

    @defer.inlineCallbacks
    def test_artists(self):
        results = yield self.spotify.artists([self.weezer_urn, self.radiohead_urn])
        self.assertTrue('artists' in results)
        self.assertTrue(len(results['artists']) == 2)

    @defer.inlineCallbacks
    def test_album_urn(self):
        album = yield self.spotify.album(self.pinkerton_urn)
        self.assertTrue(album['name'] == u'Pinkerton')

    @defer.inlineCallbacks
    def test_album_tracks(self):
        results = yield self.spotify.album_tracks(self.pinkerton_urn)
        self.assertTrue(len(results['items']) == 10)

    @defer.inlineCallbacks
    def test_albums(self):
        results = yield self.spotify.albums([self.pinkerton_urn, self.pablo_honey_urn])
        self.assertTrue('albums' in results)
        self.assertTrue(len(results['albums']) == 2)

    @defer.inlineCallbacks
    def test_track_urn(self):
        track = yield self.spotify.track(self.creep_urn)
        self.assertTrue(track['name'] == u'Creep')

    @defer.inlineCallbacks
    def test_track_id(self):
        track = yield self.spotify.track(self.creep_id)
        self.assertTrue(track['name'] == u'Creep')

    @defer.inlineCallbacks
    def test_track_url(self):
        track = yield self.spotify.track(self.creep_url)
        self.assertTrue(track['name'] == u'Creep')

    @defer.inlineCallbacks
    def test_tracks(self):
        results = yield self.spotify.tracks([self.creep_url, self.el_scorcho_urn])
        self.assertTrue('tracks' in results)
        self.assertTrue(len(results['tracks']) == 2)

    @defer.inlineCallbacks
    def test_artist_top_tracks(self):
        results = yield self.spotify.artist_top_tracks(self.weezer_urn)
        self.assertTrue('tracks' in results)
        self.assertTrue(len(results['tracks']) == 10)

    @defer.inlineCallbacks
    def test_artist_related_artists(self):
        results = yield self.spotify.artist_related_artists(self.weezer_urn)
        self.assertTrue('artists' in results)
        self.assertTrue(len(results['artists']) == 20)
        for artist in results['artists']:
            if artist['name'] == 'Rivers Cuomo':
                found = True
        self.assertTrue(found)

    @defer.inlineCallbacks
    def test_artist_search(self):
        results = yield self.spotify.search(q='weezer', type='artist')
        self.assertTrue('artists' in results)
        self.assertTrue(len(results['artists']['items']) > 0)
        self.assertTrue(results['artists']['items'][0]['name'] == 'Weezer')

    @defer.inlineCallbacks
    def test_artist_albums(self):
        results = yield self.spotify.artist_albums(self.weezer_urn)
        self.assertTrue('items' in results)
        self.assertTrue(len(results['items']) > 0)

        found = False
        for album in results['items']:
            if album['name'] == 'Hurley':
                found = True

        self.assertTrue(found)

    @defer.inlineCallbacks
    def test_album_search(self):
        results = yield self.spotify.search(q='weezer pinkerton', type='album')
        self.assertTrue('albums' in results)
        self.assertTrue(len(results['albums']['items']) > 0)
        self.assertTrue(results['albums']['items'][0]['name'].find('Pinkerton') >= 0)

    @defer.inlineCallbacks
    def test_track_search(self):
        results = yield self.spotify.search(q='el scorcho weezer', type='track')
        self.assertTrue('tracks' in results)
        self.assertTrue(len(results['tracks']['items']) > 0)
        self.assertTrue(results['tracks']['items'][0]['name'] == 'El Scorcho')

    @defer.inlineCallbacks
    def test_user(self):
        user = yield self.spotify.user(user='plamere')
        self.assertTrue(user['uri'] == 'spotify:user:plamere')

    @defer.inlineCallbacks
    def test_track_bad_id(self):
        try:
            track = yield self.spotify.track(self.bad_id)
            self.assertTrue(False)
        except spotipy_twisted.SpotifyException:
            self.assertTrue(True)

    @defer.inlineCallbacks
    def test_unauthenticated_post_fails(self):
        spotify = spotipy_twisted.Spotify()
        with self.assertRaises(SpotifyException) as cm:
            yield spotify.user_playlist_create("spotify", "Best hits of the 90s")
        self.assertEqual(cm.exception.http_status, 403)

    @defer.inlineCallbacks
    def test_custom_requests_session(self):
        from txrequests import Session

        with Session() as sess:
            sess.headers["user-agent"] = "spotipy-test"
            with_custom_session = spotipy_twisted.Spotify(requests_session=sess)
            user = yield with_custom_session.user(user="akx")
            self.assertTrue(user["uri"] == "spotify:user:akx")


'''
    Need tests for:

        - next
        - previous
'''

if __name__ == '__main__':
    import sys
    from twisted.scripts import trial

    sys.argv.extend([__name__])
    trial.run()

