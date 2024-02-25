import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint as pp
import configparser as cg

config = cg.ConfigParser()
config.read("config/secrets.cfg")

SPOTIFY_CLIENT_ID = config['Spotify']['SPOTIFY_CLIENT_ID']
SPOTIFY_CLIENT_SECRET = config['Spotify']['SPOTIFY_CLIENT_SECRET']
USER=config['Spotify']['USER']

scope = "user-top-read"
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri="http://localhost:8888/callback",
        scope=scope))

from flask import Flask, jsonify

app = Flask(__name__)

# Define a route for the API endpoint
@app.route('/api/user-info')
def get_user_info():
    # Get the user's details
    user_info = sp.user(user=USER)
    
    # Return the user_info as JSON response
    return jsonify(user_info)

if __name__ == '__main__':
    app.run(debug=True)