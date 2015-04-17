# -*- coding: latin-1 -*-

import spotipy_twisted
from  spotipy_twisted import util
from twisted.internet import defer
from twisted.trial import unittest
import pprint
import sys

'''
    Since these tests require authentication they are maintained
    separately from the other tests.

    These tests try to be benign and leave your collection and
    playlists in a relatively stable state.
'''

class AuthTestSpotipy(unittest.TestCase):
    '''
        These tests require user authentication
    '''

    playlist = "spotify:user:plamere:playlist:2oCEWyyAPbZp9xhVSxZavx"
    four_tracks = ["spotify:track:6RtPijgfPKROxEzTHNRiDp", 
                "spotify:track:7IHOIqZUUInxjVkko181PB",
                "4VrWlk8IQxevMvERoX08iC", 
                "http://open.spotify.com/track/3cySlItpiPiIAzU3NyHCJf"]

    two_tracks = ["spotify:track:6RtPijgfPKROxEzTHNRiDp", 
                "spotify:track:7IHOIqZUUInxjVkko181PB"]

    other_tracks=["spotify:track:2wySlB6vMzCbQrRnNGOYKa", 
            "spotify:track:29xKs5BAHlmlX1u4gzQAbJ",
            "spotify:track:1PB7gRWcvefzu7t3LJLUlf"]

    bad_id = 'BAD_ID'

    @defer.inlineCallbacks
    def test_track_bad_id(self):
        try:
            track = yield spotify.track(self.bad_id)
            self.assertTrue(False)
        except spotipy_twisted.SpotifyException:
            self.assertTrue(True)

    @defer.inlineCallbacks
    def test_basic_user_profile(self):
        user = yield spotify.user(username)
        self.assertTrue(user['id'] == username)

    @defer.inlineCallbacks
    def test_current_user(self):
        user = yield spotify.current_user()
        self.assertTrue(user['id'] == username)

    @defer.inlineCallbacks
    def test_me(self):
        user = yield spotify.me()
        self.assertTrue(user['id'] == username)

    @defer.inlineCallbacks
    def test_user_playlists(self):
        playlists = yield spotify.user_playlists(username, limit=5)
        self.assertTrue('items' in playlists)

        # known API issue currently causes this test to fail
        # the issue is that the API doesn't currently respect the
        # limit paramter

        self.assertTrue(len(playlists['items']) == 5)

    @defer.inlineCallbacks
    def test_user_playlist_tracks(self):
        playlists = yield spotify.user_playlists(username, limit=5)
        self.assertTrue('items' in playlists)
        for playlist in playlists['items']:
            user = playlist['owner']['id']
            pid = playlist['id']
            results = yield spotify.user_playlist_tracks(user, pid)
            self.assertTrue(len(results['items']) > 0)

    def user_playlist_tracks(self, user, playlist_id = None, fields=None, 
        limit=100, offset=0):

        # known API issue currently causes this test to fail
        # the issue is that the API doesn't currently respect the
        # limit paramter

        self.assertTrue(len(playlists['items']) == 5)

    @defer.inlineCallbacks
    def test_current_user_saved_tracks(self):
        tracks = yield spotify.current_user_saved_tracks()
        self.assertTrue(len(tracks['items']) > 0)

    @defer.inlineCallbacks
    def test_current_user_save_and_unsave_tracks(self):
        tracks = yield spotify.current_user_saved_tracks()
        total = tracks['total']

        yield spotify.current_user_saved_tracks_add(self.four_tracks)

        tracks = yield spotify.current_user_saved_tracks()
        new_total = tracks['total']
        self.assertTrue(new_total - total == len(self.four_tracks))

        tracks = yield spotify.current_user_saved_tracks_delete(self.four_tracks)
        tracks = yield spotify.current_user_saved_tracks()
        new_total = tracks['total']
        self.assertTrue(new_total == total)

    @defer.inlineCallbacks
    def test_new_releases(self):
        response = yield spotify.new_releases()
        self.assertTrue(len(response['albums']) > 0)

    @defer.inlineCallbacks
    def test_featured_releases(self):
        response = yield spotify.featured_playlists()
        self.assertTrue(len(response['playlists']) > 0)

    @defer.inlineCallbacks
    def get_or_create_spotify_playlist(self, username, playlist_name):
        playlists = yield spotify.user_playlists(username)
        while playlists:
            for item in playlists['items']:
                if item['name'] == playlist_name:
                    defer.returnValue(item['id'])
            playlists = yield spotify.next(playlists)
        playlist = yield spotify.user_playlist_create(username, playlist_name)
        playlist_id = playlist['uri']
        defer.returnValue(playlist_id)

    @defer.inlineCallbacks
    def test_user_playlist_ops(self):
        # create empty playlist
        playlist_id = yield self.get_or_create_spotify_playlist(username,
                'spotipy-testing-playlist-1')

        # remove all tracks from it

        yield spotify.user_playlist_replace_tracks(username, playlist_id,[])

        playlist = yield spotify.user_playlist(username, playlist_id)
        self.assertTrue(playlist['tracks']['total'] == 0)
        self.assertTrue(len(playlist['tracks']['items']) == 0)

        # add tracks to it

        yield spotify.user_playlist_add_tracks(username, playlist_id, self.four_tracks)
        playlist = yield spotify.user_playlist(username, playlist_id)
        self.assertTrue(playlist['tracks']['total'] == 4)
        self.assertTrue(len(playlist['tracks']['items']) == 4)

        # remove two tracks from it

        yield spotify.user_playlist_remove_all_occurrences_of_tracks (username,
                    playlist_id, self.two_tracks)

        playlist = yield spotify.user_playlist(username, playlist_id)
        self.assertTrue(playlist['tracks']['total'] == 2)
        self.assertTrue(len(playlist['tracks']['items']) == 2)

        # replace with 3 other tracks
        yield spotify.user_playlist_replace_tracks(username,
            playlist_id, self.other_tracks)

        playlist = yield spotify.user_playlist(username, playlist_id)
        self.assertTrue(playlist['tracks']['total'] == 3)
        self.assertTrue(len(playlist['tracks']['items']) == 3)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        username = sys.argv[1]
        del sys.argv[1]

        scope = 'playlist-modify-public '
        scope += 'user-library-read '
        scope += 'user-library-modify '
        scope += 'user-read-private'

        token = util.prompt_for_user_token(username, scope)
        spotify = spotipy_twisted.Spotify(auth=token)
        spotify.trace = False

        import sys
        from twisted.scripts import trial

        sys.argv.extend([__name__])
        trial.run()
    else:
        print "Usage: %s username" % (sys.argv[0],)
