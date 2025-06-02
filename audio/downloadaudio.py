import os
import zipfile
import urllib.request
import shutil
import subprocess
import urllib.parse
import sys  # <--- added to run yt-dlp as a module

# Step 1: Prepare paths and URLs
ffmpeg_url = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"
install_path = "C:\\ffmpeg"
zip_path = os.path.join(install_path, "ffmpeg.zip")
audio_output_path = os.path.abspath("audio")
os.makedirs(install_path, exist_ok=True)
os.makedirs(audio_output_path, exist_ok=True)

# Step 2: Download FFmpeg if not already present
if not os.path.exists(os.path.join(install_path, "bin", "ffmpeg.exe")):
    print("📥 Downloading FFmpeg...")
    urllib.request.urlretrieve(ffmpeg_url, zip_path)

    print("📦 Extracting FFmpeg...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(install_path)

    extracted_folder = next(
        os.path.join(install_path, f)
        for f in os.listdir(install_path)
        if os.path.isdir(os.path.join(install_path, f)) and f.startswith("ffmpeg")
    )
    bin_folder = os.path.join(extracted_folder, "bin")
    final_bin = os.path.join(install_path, "bin")

    if not os.path.exists(final_bin):
        shutil.move(bin_folder, final_bin)

# Step 3: Set temporary PATH for FFmpeg
ffmpeg_bin = os.path.join(install_path, "bin")
os.environ["PATH"] = ffmpeg_bin + os.pathsep + os.environ["PATH"]

# Step 4: Confirm FFmpeg works
print("✅ Verifying FFmpeg installation...")
subprocess.run(["ffmpeg", "-version"], check=True)

# Step 5: List of songs
songs = [
    "Kal Ho Naa Ho",
    "Kajra Re",
    "Ajeeb Dastan Hai Yeh",
    "Mehndi Laga Ke Rakhna",
    "Iktara",
    "Baharon Phool Barsao",
    "Tum Hi Ho",
    "Tera Ban Jaunga",
    "Channa Mereya",
    "Tujh Mein Rab Dikhta Hai",
    "Jeene Laga Hoon",
    "Raabta",
    "Tera Yaar Hoon Main",
    "Dil Diyan Gallan",
    "Pee Loon",
    "Sun Saathiya",
    "Galliyan",
    "Tum Mile",
    "Muskurane",
    "Shape of You",
    "Someone Like You",
    "Bohemian Rhapsody",
    "Happy",
    "Let It Be",
    "Rolling in the Deep",
    "Someone You Loved",
    "Bad Guy",
    "Thinking Out Loud",
    "Stay With Me",
    "Uptown Funk",
    "Counting Stars",
    "Firework",
    "Lose Yourself",
    "Thinking Out Loud",
    "All of Me",
    "Eye of the Tiger",
    "Perfect"
]

# Step 6: Check if yt-dlp is installed using Python module
try:
    subprocess.run([sys.executable, "-m", "yt_dlp", "--version"], check=True)
except subprocess.CalledProcessError:
    print("❌ yt-dlp is installed but returned an error")
    exit(1)
except FileNotFoundError:
    print("❌ yt-dlp is not installed. Please install it using 'pip install yt-dlp'")
    exit(1)

print(f"\n🎶 Downloading songs to: {audio_output_path}")

# Step 7: Download each song by searching on YouTube using yt-dlp as a Python module
for song in songs:
    print(f"\n➡️ Downloading '{song}'...")
    query = urllib.parse.quote(song)
    search_url = f"ytsearch1:{song}"

    try:
        subprocess.run([
            sys.executable, "-m", "yt_dlp",  # <-- run yt-dlp as python module
            "-x",
            "--audio-format", "mp3",
            "-o", os.path.join(audio_output_path, f"{song}.%(ext)s"),
            search_url
        ], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to download '{song}': {e}")

print("\n🎉 Done! Your MP3s are saved in:", audio_output_path)
