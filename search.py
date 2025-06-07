# Save this as find_missing_songs.py

# Read original list
with open('mental_health-dataset/data.xlsx', 'r', encoding='utf-8') as f:
    all_songs = set(line.strip() for line in f if line.strip())

# Read downloaded list
with open('downloaded.txt', 'r', encoding='utf-8') as f:
    downloaded_songs = set(line.strip() for line in f if line.strip())

# Find missing songs
missing_songs = all_songs - downloaded_songs

# Output missing songs
with open('missing_songs.txt', 'w', encoding='utf-8') as f:
    for song in sorted(missing_songs):
        f.write(song + '\n')

print(f"Total missing songs: {len(missing_songs)}")
print("Missing songs saved to missing_songs.txt")
