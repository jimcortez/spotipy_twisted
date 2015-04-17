from setuptools import setup

setup(
    name='spotipy-twisted',
    version='2.3.3',
    description='simple client for the Spotify Web API',
    author="@plamere",
    author_email="paul@echonest.com",
    url='http://spotipy.readthedocs.org/',
    install_requires=['txrequests'],
    license='LICENSE.txt',
    packages=['spotipy_twisted'])
