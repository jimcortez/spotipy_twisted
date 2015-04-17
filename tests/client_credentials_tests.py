# -*- coding: latin-1 -*-

import spotipy_twisted
from  spotipy_twisted.oauth2 import SpotifyClientCredentials
from twisted.internet import defer
from twisted.trial import unittest

'''
    Client Credentials Requests Tests
'''


class ClientCredentialsTestSpotipy(unittest.TestCase):
    '''
        These tests require user authentication
    '''

    muse_urn = 'spotify:artist:12Chz98pHFMPJEknJQMWvI'

    @defer.inlineCallbacks
    def test_request_with_token(self):
        artist = yield spotify.artist(self.muse_urn)
        self.assertTrue(artist['name'] == u'Muse')


if __name__ == '__main__':
    spotify_cc = SpotifyClientCredentials()
    spotify = spotipy_twisted.Spotify(client_credentials_manager=spotify_cc)
    spotify.trace = False
    import sys
    from twisted.scripts import trial

    sys.argv.extend([__name__])
    trial.run()
