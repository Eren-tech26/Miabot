import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "28269343"))
API_HASH = getenv("API_HASH", "2b01fb310b9a3ed996326c87e3ed6afd")
BOT_PRIVACY = getenv("BOT_PRIVACY", "https://telegra.ph/Privacy-Policy-for-MiaKhailfabot-10-06")
BOT_TOKEN = getenv("BOT_TOKEN", "8055158116:AAFfw3IMurfCYoAIlNE2xiBG_mjX20Mhdvo")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://anandcollage245:ZehHlJTPgnFr8AjH@cluster0.t7w7l.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 600))

LOG_GROUP_ID = int(getenv("LOG_GROUP_ID",-1002314716068))

OWNER_ID = int(getenv("OWNER_ID", 7774827065))

OWNER = int(getenv("OWNER", 7774827065))

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

HEROKU_API_KEY = getenv("HEROKU_API_KEY","HRKU-244ce902-f5e3-4c52-94d6-b5c4bb4ab7e5")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/SONGSONG220/AnieXEricaMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/aethonixsupport")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/igrischatsupport")
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "2a230af10e0a40638dc77c1febb47170")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "7f92897a59464ddbbf00f06cd6bda7fc")
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 5242880000))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 5242880000))

STRING1 = getenv("STRING_SESSION", "BQGvWx8AiqPTrwoMvjAjXvAIhPqoxpIYOUNdDQZIGPybr0Hvb-JYlPf-ObOVuEq0yaJtju2Apf5bRwQSLVeDhzQX3OXZVIvd3rEEig5AE9d6gcXFITJAgU9p9IYKHMl_XB6XQK5LRv51AOnw8m378Z1Oy1XOkzHVutzjdPYdPJwcw4veLeJx3OLx1YWQoUnym9PqnbeVS6eu8UilHIya_prYyJOocDZU_uBsMkDkUgid3XJRDfQlUEAuFy20f3m50D7awh8aB75FvmtXvEF0j0oXCQnCWSI0v0EfPFqE28QZ3Atimu5U0PI1tNk42hNe9D8aZlpcAQI-HzKEpU4ZJlVTkiFHXQAAAAGb0FjKAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv("START_IMG_URL", "https://i.ibb.co/kp7mBkT/photo-2025-02-26-17-09-29-7475776142197129224.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://i.ibb.co/Y4m9TPPq/photo-2025-02-26-17-18-33-7475778474364370948.jpg")
PLAYLIST_IMG_URL = "https://i.ibb.co/kp7mBkT/photo-2025-02-26-17-09-29-7475776142197129224.jpg"
STATS_IMG_URL = getenv("STATS_IMG_URL", "https://i.ibb.co/cS95whrC/photo-2025-02-26-17-25-12-7475780183761354756.jpg")
TELEGRAM_AUDIO_URL = "https://i.ibb.co/ZzkSgCy1/photo-2025-02-26-17-10-07-7475776318290788356.jpg"
TELEGRAM_VIDEO_URL = "https://i.ibb.co/G4nRY2Wv/photo-2025-02-26-17-10-17-7475776369830395908.jpg"
STREAM_IMG_URL = "https://i.ibb.co/5Xfhyyg4/photo-2025-02-26-17-10-48-7475776472909611036.jpg"
SOUNCLOUD_IMG_URL = "https://i.ibb.co/Hfbf9PXJ/photo-2025-02-26-17-10-57-7475776584578760708.jpg"
YOUTUBE_IMG_URL = "https://i.ibb.co/6JTN84RQ/photo-2025-02-26-17-11-34-7475776670478106628.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://i.ibb.co/q2BfZG9/photo-2025-02-26-17-12-14-7475776842276798468.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://i.ibb.co/q2BfZG9/photo-2025-02-26-17-12-14-7475776842276798468.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://i.ibb.co/q2BfZG9/photo-2025-02-26-17-12-14-7475776842276798468.jpg"

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
