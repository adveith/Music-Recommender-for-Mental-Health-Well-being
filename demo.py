import lyricsgenius
import os

# Genius API setup
genius = lyricsgenius.Genius("f79r4gtTvml2kmeDj78OZGRY8d5627AbwmKdMUv3AiDuihPD5RW4buBmgTZsrrfq", timeout=10, retries=3)
genius.skip_non_songs = True
genius.excluded_terms = ["(Remix)", "(Live)"]
genius.remove_section_headers = True

# Original list of songs
songs = [
    "Kal Ho Naa Ho", "Kajra Re", "Ajeeb Dastan Hai Yeh", "Mehndi Laga Ke Rakhna", "Iktara",
    "Baharon Phool Barsao", "Tum Hi Ho", "Tera Ban Jaunga", "Channa Mereya",
    "Tujh Mein Rab Dikhta Hai", "Jeene Laga Hoon", "Raabta", "Tera Yaar Hoon Main",
    "Dil Diyan Gallan", "Pee Loon", "Sun Saathiya", "Galliyan", "Tum Mile", "Muskurane",
    "Shape of You", "Someone Like You", "Bohemian Rhapsody", "Happy", "Let It Be",
    "Rolling in the Deep", "Someone You Loved", "Bad Guy", "Thinking Out Loud",
    "Stay With Me", "Uptown Funk", "Counting Stars", "Firework", "Lose Yourself",
    "All of Me", "Eye of the Tiger", "Perfect"
]

# Retry with artist names for failed songs
retry_with_artists = {
    "Ajeeb Dastan Hai Yeh": "Ajeeb Dastan Hai Yeh Lata Mangeshkar",
    "Baharon Phool Barsao": "Baharon Phool Barsao Mohammed Rafi"
}

output_dir = "lyrics"
os.makedirs(output_dir, exist_ok=True)

for song in songs:
    print(f"🎵 Searching for: {song}")
    try:
        song_obj = genius.search_song(song)
        if song_obj and song_obj.lyrics:
            filename = os.path.join(output_dir, f"{song}.txt")
            with open(filename, "w", encoding="utf-8") as f:
                f.write(song_obj.lyrics)
            print(f"✅ Done: {filename}")
        else:
            print(f"❌ Not found: {song}")
            # Retry with artist name if available
            if song in retry_with_artists:
                print(f"🔁 Retrying with artist: {retry_with_artists[song]}")
                retry_song_obj = genius.search_song(retry_with_artists[song])
                if retry_song_obj and retry_song_obj.lyrics:
                    filename = os.path.join(output_dir, f"{song}.txt")
                    with open(filename, "w", encoding="utf-8") as f:
                        f.write(retry_song_obj.lyrics)
                    print(f"✅ Done after retry: {filename}")
                else:
                    print(f"❌ Still not found after retry: {song}")
    except Exception as e:
        print(f"⚠️ Error for {song}: {e}")
