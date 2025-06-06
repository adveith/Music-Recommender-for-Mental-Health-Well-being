import csv

songs = [
    # 20 Hindi Songs
    {
        "song_id": 1,
        "title": "Kal Ho Naa Ho",
        "artist": "Sonu Nigam",
        "language": "Hindi",
        "lyrics": "Har ghadi badal rahi hai roop zindagi...",
        "lyrics_lang": "Hindi",
        "emotion_label": "Hopeful",
        "genre": "Bollywood",
        "release_year": 2003,
        "duration_sec": 320,
        "tempo": 90,
        "key": "C",
        "energy": 0.7,
        "valence": 0.8,
        "mfcc_mean": 0.45,
        "audio_path": "audio/kal_ho_naa_ho.mp3",
        "lyrics_path": "lyrics/kal_ho_naa_ho.txt",
    },
    {
        "song_id": 2,
        "title": "Kajra Re",
        "artist": "Alisha Chinoy, Shankar Mahadevan, Javed Ali",
        "language": "Hindi",
        "lyrics": "Kajra re kajra re tere kare kare naina...",
        "lyrics_lang": "Hindi",
        "emotion_label": "Playful",
        "genre": "Bollywood",
        "release_year": 2005,
        "duration_sec": 270,
        "tempo": 120,
        "key": "D",
        "energy": 0.85,
        "valence": 0.9,
        "mfcc_mean": 0.50,
        "audio_path": "audio/kajra_re.mp3",
        "lyrics_path": "lyrics/kajra_re.txt",
    },
    {
        "song_id": 3,
        "title": "Ajeeb Dastan Hai Yeh",
        "artist": "Lata Mangeshkar",
        "language": "Hindi",
        "lyrics": "Ajeeb dastan hai yeh, kahan shuru kahan khatam...",
        "lyrics_lang": "Hindi",
        "emotion_label": "Melancholic",
        "genre": "Bollywood",
        "release_year": 1960,
        "duration_sec": 240,
        "tempo": 85,
        "key": "F",
        "energy": 0.4,
        "valence": 0.3,
        "mfcc_mean": 0.40,
        "audio_path": "audio/ajeeb_dastan_hai_yeh.mp3",
        "lyrics_path": "lyrics/ajeeb_dastan_hai_yeh.txt",
    },
    {
        "song_id": 4,
        "title": "Mehndi Laga Ke Rakhna",
        "artist": "Lata Mangeshkar, Udit Narayan",
        "language": "Hindi",
        "lyrics": "Mehndi laga ke rakhna doli saja ke rakhna...",
        "lyrics_lang": "Hindi",
        "emotion_label": "Festive",
        "genre": "Bollywood",
        "release_year": 1994,
        "duration_sec": 300,
        "tempo": 110,
        "key": "G",
        "energy": 0.75,
        "valence": 0.9,
        "mfcc_mean": 0.52,
        "audio_path": "audio/mehndi_laga_ke_rakhna.mp3",
        "lyrics_path": "lyrics/mehndi_laga_ke_rakhna.txt",
    },
    {
        "song_id": 5,
        "title": "Iktara",
        "artist": "Kavita Seth, Amitabh Bhattacharya",
        "language": "Hindi",
        "lyrics": "Ik tara bole to kya bole...",
        "lyrics_lang": "Hindi",
        "emotion_label": "Calm",
        "genre": "Bollywood",
        "release_year": 2008,
        "duration_sec": 250,
        "tempo": 75,
        "key": "A",
        "energy": 0.5,
        "valence": 0.6,
        "mfcc_mean": 0.44,
        "audio_path": "audio/iktara.mp3",
        "lyrics_path": "lyrics/iktara.txt",
    },
    {
        "song_id": 6,
        "title": "Baharon Phool Barsao",
        "artist": "Mohammed Rafi",
        "language": "Hindi",
        "lyrics": "Baharon phool barsao, mera mehboob aaya hai...",
        "lyrics_lang": "Hindi",
        "emotion_label": "Romantic",
        "genre": "Bollywood",
        "release_year": 1966,
        "duration_sec": 280,
        "tempo": 95,
        "key": "E",
        "energy": 0.6,
        "valence": 0.7,
        "mfcc_mean": 0.47,
        "audio_path": "audio/baharon_phool_barsao.mp3",
        "lyrics_path": "lyrics/baharon_phool_barsao.txt",
    },
    {
        "song_id": 7,
        "title": "Tum Hi Ho",
        "artist": "Arijit Singh",
        "language": "Hindi",
        "lyrics": "Hum tere bin ab reh nahi sakte...",
        "lyrics_lang": "Hindi",
        "emotion_label": "Romantic",
        "genre": "Bollywood",
        "release_year": 2013,
        "duration_sec": 350,
        "tempo": 65,
        "key": "B",
        "energy": 0.55,
        "valence": 0.6,
        "mfcc_mean": 0.49,
        "audio_path": "audio/tum_hi_ho.mp3",
        "lyrics_path": "lyrics/tum_hi_ho.txt",
    },
    {
        "song_id": 8,
        "title": "Tera Ban Jaunga",
        "artist": "Akhil Sachdeva, Tulsi Kumar",
        "language": "Hindi",
        "lyrics": "Main tera ban jaunga...",
        "lyrics_lang": "Hindi",
        "emotion_label": "Romantic",
        "genre": "Bollywood",
        "release_year": 2018,
        "duration_sec": 280,
        "tempo": 70,
        "key": "C",
        "energy": 0.6,
        "valence": 0.7,
        "mfcc_mean": 0.46,
        "audio_path": "audio/tera_ban_jaunga.mp3",
        "lyrics_path": "lyrics/tera_ban_jaunga.txt",
    },
    {
        "song_id": 9,
        "title": "Channa Mereya",
        "artist": "Arijit Singh",
        "language": "Hindi",
        "lyrics": "Acha chalta hoon...",
        "lyrics_lang": "Hindi",
        "emotion_label": "Sad",
        "genre": "Bollywood",
        "release_year": 2016,
        "duration_sec": 330,
        "tempo": 60,
        "key": "D",
        "energy": 0.4,
        "valence": 0.3,
        "mfcc_mean": 0.42,
        "audio_path": "audio/channa_mereya.mp3",
        "lyrics_path": "lyrics/channa_mereya.txt",
    },
    {
        "song_id": 10,
        "title": "Tujh Mein Rab Dikhta Hai",
        "artist": "Roop Kumar Rathod",
        "language": "Hindi",
        "lyrics": "Tujh mein rab dikhta hai...",
        "lyrics_lang": "Hindi",
        "emotion_label": "Devotional",
        "genre": "Bollywood",
        "release_year": 2008,
        "duration_sec": 310,
        "tempo": 80,
        "key": "G",
        "energy": 0.5,
        "valence": 0.6,
        "mfcc_mean": 0.48,
        "audio_path": "audio/tujh_mein_rab_dikhta_hai.mp3",
        "lyrics_path": "lyrics/tujh_mein_rab_dikhta_hai.txt",
    },
    {
        "song_id": 11,
        "title": "Jeene Laga Hoon",
        "artist": "Atif Aslam, Shreya Ghoshal",
        "language": "Hindi",
        "lyrics": "Jeene laga hoon pehle se zyada...",
        "lyrics_lang": "Hindi",
        "emotion_label": "Romantic",
        "genre": "Bollywood",
        "release_year": 2009,
        "duration_sec": 295,
        "tempo": 85,
        "key": "A",
        "energy": 0.6,
        "valence": 0.7,
        "mfcc_mean": 0.47,
        "audio_path": "audio/jeene_laga_hoon.mp3",
        "lyrics_path": "lyrics/jeene_laga_hoon.txt",
    },
    {
        "song_id": 12,
        "title": "Raabta",
        "artist": "Arijit Singh",
        "language": "Hindi",
        "lyrics": "Kehte hain khuda ne is jahan mein sabhi ke liye...",
        "lyrics_lang": "Hindi",
        "emotion_label": "Romantic",
        "genre": "Bollywood",
        "release_year": 2012,
        "duration_sec": 300,
        "tempo": 75,
        "key": "C",
        "energy": 0.55,
        "valence": 0.65,
        "mfcc_mean": 0.45,
        "audio_path": "audio/raabta.mp3",
        "lyrics_path": "lyrics/raabta.txt",
    },
    {
        "song_id": 13,
        "title": "Tera Yaar Hoon Main",
        "artist": "Arijit Singh",
        "language": "Hindi",
        "lyrics": "Tera yaar hoon main...",
        "lyrics_lang": "Hindi",
        "emotion_label": "Friendship",
        "genre": "Bollywood",
        "release_year": 2018,
        "duration_sec": 310,
        "tempo": 90,
        "key": "B",
        "energy": 0.7,
        "valence": 0.8,
        "mfcc_mean": 0.50,
        "audio_path": "audio/tera_yaar_hoon_main.mp3",
        "lyrics_path": "lyrics/tera_yaar_hoon_main.txt",
    },
    {
        "song_id": 14,
        "title": "Dil Diyan Gallan",
        "artist": "Atif Aslam",
        "language": "Hindi",
        "lyrics": "Dil diyan gallan...",
        "lyrics_lang": "Hindi",
        "emotion_label": "Romantic",
        "genre": "Bollywood",
        "release_year": 2017,
        "duration_sec": 305,
        "tempo": 85,
        "key": "F",
        "energy": 0.6,
        "valence": 0.7,
        "mfcc_mean": 0.48,
        "audio_path": "audio/dil_diyan_gallan.mp3",
        "lyrics_path": "lyrics/dil_diyan_gallan.txt",
    },
    {
        "song_id": 15,
        "title": "Pee Loon",
        "artist": "Mohit Chauhan",
        "language": "Hindi",
        "lyrics": "Tere bina beswaadi beswaadi raat meri...",
        "lyrics_lang": "Hindi",
        "emotion_label": "Romantic",
        "genre": "Bollywood",
        "release_year": 2010,
        "duration_sec": 290,
        "tempo": 80,
        "key": "E",
        "energy": 0.5,
        "valence": 0.6,
        "mfcc_mean": 0.45,
        "audio_path": "audio/pee_loon.mp3",
        "lyrics_path": "lyrics/pee_loon.txt",
    },
    {
        "song_id": 16,
        "title": "Sun Saathiya",
        "artist": "Priya Saraiya, Divya Kumar",
        "language": "Hindi",
        "lyrics": "Sun saathiya...",
        "lyrics_lang": "Hindi",
        "emotion_label": "Romantic",
        "genre": "Bollywood",
        "release_year": 2015,
        "duration_sec": 320,
        "tempo": 95,
        "key": "C",
        "energy": 0.65,
        "valence": 0.75,
        "mfcc_mean": 0.50,
        "audio_path": "audio/sun_saathiya.mp3",
        "lyrics_path": "lyrics/sun_saathiya.txt",
    },
    {
        "song_id": 17,
        "title": "Galliyan",
        "artist": "Ankit Tiwari",
        "language": "Hindi",
        "lyrics": "Galliyan galliyan teri galliyan...",
        "lyrics_lang": "Hindi",
        "emotion_label": "Romantic",
        "genre": "Bollywood",
        "release_year": 2014,
        "duration_sec": 300,
        "tempo": 90,
        "key": "G",
        "energy": 0.6,
        "valence": 0.7,
        "mfcc_mean": 0.48,
        "audio_path": "audio/galliyan.mp3",
        "lyrics_path": "lyrics/galliyan.txt",
    },
    {
        "song_id": 18,
        "title": "Tum Mile",
        "artist": "Neeraj Shridhar",
        "language": "Hindi",
        "lyrics": "Tum mile to...",
        "lyrics_lang": "Hindi",
        "emotion_label": "Romantic",
        "genre": "Bollywood",
        "release_year": 2009,
        "duration_sec": 280,
        "tempo": 85,
        "key": "A",
        "energy": 0.55,
        "valence": 0.65,
        "mfcc_mean": 0.46,
        "audio_path": "audio/tum_mile.mp3",
        "lyrics_path": "lyrics/tum_mile.txt",
    },
    {
        "song_id": 19,
        "title": "Muskurane",
        "artist": "Arijit Singh",
        "language": "Hindi",
        "lyrics": "Muskurane ki wajah tum ho...",
        "lyrics_lang": "Hindi",
        "emotion_label": "Romantic",
        "genre": "Bollywood",
        "release_year": 2014,
        "duration_sec": 310,
        "tempo": 75,
        "key": "B",
        "energy": 0.6,
        "valence": 0.7,
        "mfcc_mean": 0.49,
        "audio_path": "audio/muskurane.mp3",
        "lyrics_path": "lyrics/muskurane.txt",
    },
      {
        "song_id": 20,
        "title": "Tum Mile",
        "artist": "Neeraj Shridhar",
        "language": "Hindi",
        "lyrics": "Tum mile to mil gaya yeh jahaan...",
        "lyrics_lang": "Hindi",
        "emotion_label": "Romantic",
        "genre": "Bollywood",
        "release_year": 2009,
        "duration_sec": 290,
        "tempo": 85,
        "key": "F",
        "energy": 0.55,
        "valence": 0.65,
        "mfcc_mean": 0.46,
        "audio_path": "audio/tum_mile.mp3",
        "lyrics_path": "lyrics/tum_mile.txt",
    },
    # 20 English Songs
     {
        "song_id": 21,
        "title": "Shape of You",
        "artist": "Ed Sheeran",
        "language": "English",
        "lyrics": "The club isn't the best place to find a lover...",
        "lyrics_lang": "English",
        "emotion_label": "Energetic",
        "genre": "Pop",
        "release_year": 2017,
        "duration_sec": 240,
        "tempo": 96,
        "key": "C#",
        "energy": 0.8,
        "valence": 0.9,
        "mfcc_mean": 0.52,
        "audio_path": "audio/shape_of_you.mp3",
        "lyrics_path": "lyrics/shape_of_you.txt",
    },
    {
        "song_id": 22,
        "title": "Someone Like You",
        "artist": "Adele",
        "language": "English",
        "lyrics": "I heard that you're settled down...",
        "lyrics_lang": "English",
        "emotion_label": "Melancholic",
        "genre": "Pop",
        "release_year": 2011,
        "duration_sec": 285,
        "tempo": 67,
        "key": "A",
        "energy": 0.4,
        "valence": 0.3,
        "mfcc_mean": 0.45,
        "audio_path": "audio/someone_like_you.mp3",
        "lyrics_path": "lyrics/someone_like_you.txt",
    },
    {
        "song_id": 23,
        "title": "Bohemian Rhapsody",
        "artist": "Queen",
        "language": "English",
        "lyrics": "Is this the real life? Is this just fantasy?...",
        "lyrics_lang": "English",
        "emotion_label": "Dramatic",
        "genre": "Rock",
        "release_year": 1975,
        "duration_sec": 355,
        "tempo": 72,
        "key": "Bb",
        "energy": 0.7,
        "valence": 0.6,
        "mfcc_mean": 0.53,
        "audio_path": "audio/bohemian_rhapsody.mp3",
        "lyrics_path": "lyrics/bohemian_rhapsody.txt",
    },
    {
        "song_id": 24,
        "title": "Happy",
        "artist": "Pharrell Williams",
        "language": "English",
        "lyrics": "Because I'm happy...",
        "lyrics_lang": "English",
        "emotion_label": "Happy",
        "genre": "Pop",
        "release_year": 2013,
        "duration_sec": 233,
        "tempo": 160,
        "key": "F",
        "energy": 0.9,
        "valence": 0.95,
        "mfcc_mean": 0.6,
        "audio_path": "audio/happy.mp3",
        "lyrics_path": "lyrics/happy.txt",
    },
    {
        "song_id": 25,
        "title": "Let It Be",
        "artist": "The Beatles",
        "language": "English",
        "lyrics": "When I find myself in times of trouble...",
        "lyrics_lang": "English",
        "emotion_label": "Calm",
        "genre": "Rock",
        "release_year": 1970,
        "duration_sec": 243,
        "tempo": 72,
        "key": "C",
        "energy": 0.5,
        "valence": 0.6,
        "mfcc_mean": 0.48,
        "audio_path": "audio/let_it_be.mp3",
        "lyrics_path": "lyrics/let_it_be.txt",
    },
    {
        "song_id": 26,
        "title": "Rolling in the Deep",
        "artist": "Adele",
        "language": "English",
        "lyrics": "There's a fire starting in my heart...",
        "lyrics_lang": "English",
        "emotion_label": "Powerful",
        "genre": "Pop",
        "release_year": 2010,
        "duration_sec": 228,
        "tempo": 105,
        "key": "C",
        "energy": 0.85,
        "valence": 0.55,
        "mfcc_mean": 0.55,
        "audio_path": "audio/rolling_in_the_deep.mp3",
        "lyrics_path": "lyrics/rolling_in_the_deep.txt",
    },
    {
        "song_id": 27,
        "title": "Someone You Loved",
        "artist": "Lewis Capaldi",
        "language": "English",
        "lyrics": "I'm going under and this time I fear there's no one to save me...",
        "lyrics_lang": "English",
        "emotion_label": "Sad",
        "genre": "Pop",
        "release_year": 2018,
        "duration_sec": 182,
        "tempo": 110,
        "key": "F",
        "energy": 0.3,
        "valence": 0.25,
        "mfcc_mean": 0.42,
        "audio_path": "audio/someone_you_loved.mp3",
        "lyrics_path": "lyrics/someone_you_loved.txt",
    },
    {
        "song_id": 28,
        "title": "Bad Guy",
        "artist": "Billie Eilish",
        "language": "English",
        "lyrics": "So you're a tough guy...",
        "lyrics_lang": "English",
        "emotion_label": "Playful",
        "genre": "Pop",
        "release_year": 2019,
        "duration_sec": 194,
        "tempo": 135,
        "key": "G#",
        "energy": 0.8,
        "valence": 0.7,
        "mfcc_mean": 0.58,
        "audio_path": "audio/bad_guy.mp3",
        "lyrics_path": "lyrics/bad_guy.txt",
    },
    {
        "song_id": 29,
        "title": "Thinking Out Loud",
        "artist": "Ed Sheeran",
        "language": "English",
        "lyrics": "When your legs don't work like they used to before...",
        "lyrics_lang": "English",
        "emotion_label": "Romantic",
        "genre": "Pop",
        "release_year": 2014,
        "duration_sec": 281,
        "tempo": 79,
        "key": "D",
        "energy": 0.6,
        "valence": 0.75,
        "mfcc_mean": 0.5,
        "audio_path": "audio/thinking_out_loud.mp3",
        "lyrics_path": "lyrics/thinking_out_loud.txt",
    },
    {
        "song_id": 30,
        "title": "Stay With Me",
        "artist": "Sam Smith",
        "language": "English",
        "lyrics": "Guess it's true, I'm not good at a one-night stand...",
        "lyrics_lang": "English",
        "emotion_label": "Sad",
        "genre": "Soul",
        "release_year": 2014,
        "duration_sec": 172,
        "tempo": 84,
        "key": "A",
        "energy": 0.4,
        "valence": 0.3,
        "mfcc_mean": 0.44,
        "audio_path": "audio/stay_with_me.mp3",
        "lyrics_path": "lyrics/stay_with_me.txt",
    },
    {
        "song_id": 31,
        "title": "Uptown Funk",
        "artist": "Mark Ronson ft. Bruno Mars",
        "language": "English",
        "lyrics": "This hit, that ice cold...",
        "lyrics_lang": "English",
        "emotion_label": "Energetic",
        "genre": "Funk",
        "release_year": 2014,
        "duration_sec": 270,
        "tempo": 115,
        "key": "D#",
        "energy": 0.9,
        "valence": 0.95,
        "mfcc_mean": 0.6,
        "audio_path": "audio/uptown_funk.mp3",
        "lyrics_path": "lyrics/uptown_funk.txt",
    },
    {
        "song_id": 32,
        "title": "Someone Like You",
        "artist": "Adele",
        "language": "English",
        "lyrics": "I heard that you're settled down...",
        "lyrics_lang": "English",
        "emotion_label": "Melancholic",
        "genre": "Pop",
        "release_year": 2011,
        "duration_sec": 285,
        "tempo": 67,
        "key": "A",
        "energy": 0.4,
        "valence": 0.3,
        "mfcc_mean": 0.45,
        "audio_path": "audio/someone_like_you.mp3",
        "lyrics_path": "lyrics/someone_like_you.txt",
    },
    {
        "song_id": 33,
        "title": "Counting Stars",
        "artist": "OneRepublic",
        "language": "English",
        "lyrics": "Lately, I've been, I've been losing sleep...",
        "lyrics_lang": "English",
        "emotion_label": "Hopeful",
        "genre": "Pop",
        "release_year": 2013,
        "duration_sec": 257,
        "tempo": 122,
        "key": "C#m",
        "energy": 0.75,
        "valence": 0.8,
        "mfcc_mean": 0.56,
        "audio_path": "audio/counting_stars.mp3",
        "lyrics_path": "lyrics/counting_stars.txt",
    },
    {
        "song_id": 34,
        "title": "Firework",
        "artist": "Katy Perry",
        "language": "English",
        "lyrics": "Do you ever feel like a plastic bag...",
        "lyrics_lang": "English",
        "emotion_label": "Inspiring",
        "genre": "Pop",
        "release_year": 2010,
        "duration_sec": 228,
        "tempo": 124,
        "key": "G#",
        "energy": 0.85,
        "valence": 0.9,
        "mfcc_mean": 0.59,
        "audio_path": "audio/firework.mp3",
        "lyrics_path": "lyrics/firework.txt",
    },
    {
        "song_id": 35,
        "title": "Lose Yourself",
        "artist": "Eminem",
        "language": "English",
        "lyrics": "Look, if you had one shot...",
        "lyrics_lang": "English",
        "emotion_label": "Motivational",
        "genre": "Rap",
        "release_year": 2002,
        "duration_sec": 326,
        "tempo": 171,
        "key": "D#m",
        "energy": 0.95,
        "valence": 0.7,
        "mfcc_mean": 0.65,
        "audio_path": "audio/lose_yourself.mp3",
        "lyrics_path": "lyrics/lose_yourself.txt",
    },
    {
        "song_id": 36,
        "title": "All of Me",
        "artist": "John Legend",
        "language": "English",
        "lyrics": "What would I do without your smart mouth...",
        "lyrics_lang": "English",
        "emotion_label": "Romantic",
        "genre": "R&B",
        "release_year": 2013,
        "duration_sec": 269,
        "tempo": 120,
        "key": "Ab",
        "energy": 0.5,
        "valence": 0.7,
        "mfcc_mean": 0.48,
        "audio_path": "audio/all_of_me.mp3",
        "lyrics_path": "lyrics/all_of_me.txt",
    },
    {
        "song_id": 37,
        "title": "Eye of the Tiger",
        "artist": "Survivor",
        "language": "English",
        "lyrics": "Risin' up, back on the street...",
        "lyrics_lang": "English",
        "emotion_label": "Motivational",
        "genre": "Rock",
        "release_year": 1982,
        "duration_sec": 245,
        "tempo": 109,
        "key": "C",
        "energy": 0.9,
        "valence": 0.85,
        "mfcc_mean": 0.6,
        "audio_path": "audio/eye_of_the_tiger.mp3",
        "lyrics_path": "lyrics/eye_of_the_tiger.txt",
    },
    {
        "song_id": 38,
        "title": "Thinking Out Loud",
        "artist": "Ed Sheeran",
        "language": "English",
        "lyrics": "When your legs don't work like they used to before...",
        "lyrics_lang": "English",
        "emotion_label": "Romantic",
        "genre": "Pop",
        "release_year": 2014,
        "duration_sec": 281,
        "tempo": 79,
        "key": "D",
        "energy": 0.6,
        "valence": 0.75,
        "mfcc_mean": 0.5,
        "audio_path": "audio/thinking_out_loud.mp3",
        "lyrics_path": "lyrics/thinking_out_loud.txt",
    },
    {
        "song_id": 39,
        "title": "Perfect",
        "artist": "Ed Sheeran",
        "language": "English",
        "lyrics": "I found a love for me...",
        "lyrics_lang": "English",
        "emotion_label": "Romantic",
        "genre": "Pop",
        "release_year": 2017,
        "duration_sec": 263,
        "tempo": 63,
        "key": "Ab",
        "energy": 0.5,
        "valence": 0.8,
        "mfcc_mean": 0.49,
        "audio_path": "audio/perfect.mp3",
        "lyrics_path": "lyrics/perfect.txt",
    },
    {
        "song_id": 40,
        "title": "Counting Stars",
        "artist": "OneRepublic",
        "language": "English",
        "lyrics": "Lately, I've been, I've been losing sleep...",
        "lyrics_lang": "English",
        "emotion_label": "Hopeful",
        "genre": "Pop",
        "release_year": 2013,
        "duration_sec": 257,
        "tempo": 122,
        "key": "C#m",
        "energy": 0.75,
        "valence": 0.8,
        "mfcc_mean": 0.56,
        "audio_path": "audio/counting_stars.mp3",
        "lyrics_path": "lyrics/counting_stars.txt",
    },
]
csv_file = r"mental_health-dataset\songs_dataset.csv"

# Get the headers from the keys of the first song dictionary
headers = songs[0].keys()

# Write to CSV
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(songs)

print(f"CSV file '{csv_file}' has been created and saved successfully.")