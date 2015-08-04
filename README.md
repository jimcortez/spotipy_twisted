# spotipy_twisted - a Python client for The Spotify Web API

[![TravisCI Build Status](https://travis-ci.org/jimcortez/spotipy_twisted.svg?branch=master)](https://travis-ci.org/jimcortez/spotipy_twisted)

## Description

This is a forked package from https://github.com/plamere/spotipy (Version 2.3.3)
It uses treq to take advantage of twisted: https://github.com/twisted/treq

Spotipy is a thin client library for the Spotify Web API.

## Documentation

The usage of this library is identical to spotipy, except for the use of twisted deferreds. 
Simply add the "@defer.inlineCallbacks" decorator to any function calling a spotipy method, then yield to the result.
See Quick Start for an example.

Spotipy's full documentation is online at [Spotipy Documentation](http://spotipy.readthedocs.org/)


## Installation
If you already have [Python](http://www.python.org/) on your system you can install the library simply by downloading the distribution, unpack it and install in the usual fashion:

    python setup.py install

You can also install it using a popular package manager with 

  `pip install spotipy_twisted`

or

  `easy_install spotipy_twisted`


## Dependencies

- [treq](https://github.com/twisted/treq) - spotipy requires the treq package to be installed


## Quick Start
To get started, simply install spotipy_twisted, create a Spotify object and call methods:

    from twisted.internet import reactor, defer
    import spotipy_twisted
    sp = spotipy_twisted.Spotify()
    
    @defer.inlineCallbacks
    def search(query):
        results = yield sp.search(q=query, limit=20)
        for i, t in enumerate(results['tracks']['items']):
            print ' ', i, t['name']
        reactor.stop()
    
    search('Michael Franti')
    reactor.run()


A full set of examples can be found in the [online documentation](http://spotipy.readthedocs.org/) and in the [Spotipy examples directory](https://github.com/plamere/spotipy/tree/master/examples).
        

## Reporting Issues

If you have suggestions, bugs or other issues specific to this library, file them [here](https://github.com/jimcortez/spotipy_twisted/issues). Or just send me a pull request.

## Version

1.0, April 17, 2015    -- Forked spotipy 2.3.3, initial release
