from setuptools import setup

setup(
    name='spotipy-twisted',
    version='1.0',
    description='simple client for the Spotify Web API',
    author="@jecortez",
    author_email="jecortez@helloivee.com",
    url='http://spotipy.readthedocs.org/',
    install_requires=['treq'],
    license='LICENSE.txt',
    packages=['spotipy_twisted'])
