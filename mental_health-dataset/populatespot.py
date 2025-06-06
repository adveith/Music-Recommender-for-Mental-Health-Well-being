import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import time
import random
import os

# ---- CONFIGURATION ----
SPOTIFY_CLIENT_ID = '04f7247cf5a54212b06730568b6e7afc'
SPOTIFY_CLIENT_SECRET = '8534f65d763c41ac99384eb22623ae5a'
BATCH_SIZE = 1000
OUTPUT_FILE = 'music_dataset.xlsx'

sp = spotipy.Spotify(
    client_credentials_manager=SpotifyClientCredentials(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET
    )
)

columns = [
    'song_id', 'title', 'artist', 'language', 'Hybrid_RecSys',
    'collaborative_filtering', 'context', 'instrumentation', 'mood_tags',
    'status', 'lyrics', 'emotion_label', 'genre', 'release_year',
    'duration_sec', 'tempo', 'key', 'energy', 'valence', 'mfcc_mean',
    'audio_path', 'lyrics_path'
]

def fetch_playlist_ids(limit=50):
    playlist_ids = []
    keywords = [
        'pop', 'rock', 'chill', 'focus', 'happy', 'calm',
        'relax', 'study', 'party', 'sleep', 'jazz', 'classical'
    ]
    for kw in keywords:
        try:
            results = sp.search(q=kw, type='playlist', limit=5)
            if results and 'playlists' in results and 'items' in results['playlists']:
                for pl in results['playlists']['items']:
                    if pl['id'] not in playlist_ids:
                        playlist_ids.append(pl['id'])
            if len(playlist_ids) >= limit:
                break
        except Exception as e:
            print(f"Error searching for {kw}: {e}")
    return playlist_ids[:limit]

def fetch_songs_from_playlist(playlist_id):
    tracks = []
    try:
        results = sp.playlist_tracks(playlist_id)
        tracks.extend(results['items'])
        while results['next']:
            results = sp.next(results)
            tracks.extend(results['items'])
    except Exception as e:
        print(f"Error fetching playlist {playlist_id}: {str(e)}")
    return tracks

def load_existing_song_ids():
    if os.path.exists(OUTPUT_FILE):
        df_existing = pd.read_excel(OUTPUT_FILE)
        return set(df_existing['audio_path'].apply(lambda x: x.split('/')[-1].replace('.mp3', '')))
    return set()

def build_dataset(batch_size=1000):
    existing_song_ids = load_existing_song_ids()
    print(f"Already have {len(existing_song_ids)} songs. Collecting {batch_size} more...")

    playlist_ids = fetch_playlist_ids(limit=50)
    song_ids_collected = set()
    songs_data = []

    start_song_id = len(existing_song_ids) + 1

    for playlist_id in playlist_ids:
        if len(song_ids_collected) >= batch_size:
            break

        print(f"\nProcessing playlist: {playlist_id}")
        tracks = fetch_songs_from_playlist(playlist_id)

        for item in tracks:
            if len(song_ids_collected) >= batch_size:
                break

            track = item.get('track')
            if not track or not track.get('id'):
                continue

            track_id = track['id']
            if track_id in existing_song_ids or track_id in song_ids_collected:
                continue

            try:
                artist = track['artists'][0]['name']
                genre = 'Unknown'
                try:
                    artist_info = sp.artist(track['artists'][0]['id'])
                    genre = artist_info['genres'][0] if artist_info['genres'] else 'Unknown'
                except:
                    pass

                # These will be blank/default since you can't get them from audio-features
                tempo = ''
                key = ''
                energy = ''
                valence = ''
                mfcc_mean = ''

                row = [
                    start_song_id + len(song_ids_collected),
                    track['name'],
                    artist,
                    'English',
                    'Yes',
                    'Yes',
                    '',  # context
                    '',  # instrumentation
                    '',  # mood_tags
                    'active',
                    '',
                    '',  # emotion_label
                    genre,
                    int(track['album']['release_date'][:4]) if track['album']['release_date'] else '',
                    int(track['duration_ms'] / 1000),
                    tempo,
                    key,
                    energy,
                    valence,
                    mfcc_mean,
                    f'audio/{track_id}.mp3',
                    f'lyrics/{track_id}.txt'
                ]

                songs_data.append(row)
                song_ids_collected.add(track_id)
                print(f"Collected: {len(song_ids_collected)}/{batch_size}", end='\r')
                time.sleep(0.15)

            except Exception as e:
                print(f"Error processing track {track_id}: {str(e)}")
                continue

    df_new = pd.DataFrame(songs_data, columns=columns)
    if os.path.exists(OUTPUT_FILE):
        df_existing = pd.read_excel(OUTPUT_FILE)
        df_combined = pd.concat([df_existing, df_new], ignore_index=True)
        df_combined.to_excel(OUTPUT_FILE, index=False)
    else:
        df_new.to_excel(OUTPUT_FILE, index=False)
    print(f"\nBatch of {len(songs_data)} songs saved to {OUTPUT_FILE}")

if __name__ == '__main__':
    build_dataset(BATCH_SIZE)
