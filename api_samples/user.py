from flask import Flask, jsonify

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint as pp

# Define the required scope
scope = "user-top-read"

import configparser as cg

config = cg.ConfigParser()
config.read("config/secrets.cfg")

SPOTIFY_CLIENT_ID = config['Spotify']['SPOTIFY_CLIENT_ID']
SPOTIFY_CLIENT_SECRET = config['Spotify']['SPOTIFY_CLIENT_SECRET']
USER=config['Spotify']['USER']

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri="http://localhost:8888/callback",
        scope=scope))

# Get the user's details
user_info = sp.user(user=USER)
pp.pprint(user_info)