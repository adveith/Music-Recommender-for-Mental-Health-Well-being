import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
import urllib.parse

def search_genius_url(artist, title):
    query = urllib.parse.quote(f"{artist} {title} lyrics")
    url = f"https://genius.com/api/search/multi?per_page=1&q={query}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return None
    json_data = response.json()
    sections = json_data.get("response", {}).get("sections", [])
    for section in sections:
        for hit in section.get("hits", []):
            if hit.get("type") == "song":
                return hit.get("result", {}).get("url")
    return None

def get_lyrics_from_url(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return "Lyrics not found"
    soup = BeautifulSoup(response.text, "html.parser")
    lyrics_divs = soup.select("div[class^='Lyrics__Container']")
    lyrics = ""
    for div in lyrics_divs:
        for br in div.find_all("br"):
            br.replace_with("\n")
        lyrics += div.get_text(separator="\n").strip() + "\n"
    return lyrics.strip() if lyrics else "Lyrics not found"

# Load CSV
df = pd.read_excel(r"mental_health-dataset\data.xlsx")
  # Make sure this is correct path

results = []

for index, row in df.iterrows():
    artist = str(row.get("artist", "")).strip()
    title = str(row.get("title", "")).strip()
    print(f"[{index+1}] Fetching: {title} by {artist}")
    if not artist or not title:
        lyrics = "Missing artist or title"
    else:
        try:
            url = search_genius_url(artist, title)
            lyrics = get_lyrics_from_url(url) if url else "Lyrics not found"
        except Exception as e:
            lyrics = f"Error: {str(e)}"
    results.append({"title": title, "artist": artist, "lyrics": lyrics})
    time.sleep(2)

output_df = pd.DataFrame(results)
output_df.to_csv("lyrics_output.csv", index=False, encoding="utf-8-sig")
