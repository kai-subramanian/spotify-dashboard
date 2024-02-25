import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Define the required scope
import configparser as cg

config = cg.ConfigParser()
config.read("config/secrets.cfg")

SPOTIFY_CLIENT_ID = config['Spotify']['SPOTIFY_CLIENT_ID']
SPOTIFY_CLIENT_SECRET = config['Spotify']['SPOTIFY_CLIENT_SECRET']
scope="user-top-read"
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri="http://localhost:8888/callback",
        scope=scope))

# Get the user's top artists
top_artists = sp.current_user_top_artists(limit=10, time_range='medium_term')  # You can adjust the limit and time_range as needed
import pprint as pp
print("Your Top Tracks:")
pp.pprint(top_artists)