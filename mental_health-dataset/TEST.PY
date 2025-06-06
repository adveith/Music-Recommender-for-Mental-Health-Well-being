import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
    client_id='04f7247cf5a54212b06730568b6e7afc',
    client_secret='8534f65d763c41ac99384eb22623ae5a'
))

# Try a known popular track ID
track_id = '3n3Ppam7vgaVa1iaRUc9Lp'  # "Mr. Brightside" by The Killers
try:
    features = sp.audio_features([track_id])
    print(features)
except Exception as e:
    print("Error:", e)
