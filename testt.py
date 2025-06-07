import os
import pandas as pd
import lyricsgenius

# ✅ Set your Genius API token
GENIUS_ACCESS_TOKEN = "f79r4gtTvml2kmeDj78OZGRY8d5627AbwmKdMUv3AiDuihPD5RW4buBmgTZsrrfq"  # Replace with your token
genius = lyricsgenius.Genius(GENIUS_ACCESS_TOKEN)
genius.skip_non_songs = True
genius.excluded_terms = ["(Remix)", "(Live)"]
genius.remove_section_headers = True

# ✅ Define lyrics folder path
lyrics_folder = os.path.abspath("lyrics")
os.makedirs(lyrics_folder, exist_ok=True)

# ✅ Load songs from Excel file
excel_path = "mental_health-dataset\data.xlsx"  # Make sure your Excel file is saved with this name
df = pd.read_excel(excel_path)

print(f"\n📥 Saving lyrics to: {lyrics_folder}")

# ✅ Loop through each row and fetch lyrics
for index, row in df.iterrows():
    title = str(row["title"]).strip()
    artist = str(row["artist"]).strip()

    print(f"\n🔍 Fetching lyrics for: {title} by {artist}")
    try:
        # In case multiple artists are listed, use the first one for the Genius API
        main_artist = artist.split(",")[0].strip()

        song = genius.search_song(title, main_artist)
        if song and song.lyrics:
            safe_filename = "".join(c for c in f"{title} - {main_artist}" if c.isalnum() or c in (" ", "_", "-")).rstrip()
            file_path = os.path.join(lyrics_folder, f"{safe_filename}.txt")
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(song.lyrics)
            print(f"✅ Saved: {file_path}")
        else:
            print(f"❌ Lyrics not found for: {title} by {artist}")
    except Exception as e:
        print(f"⚠️ Error fetching '{title}' by '{artist}': {e}")

print("\n🎉 Lyrics fetching complete.")
