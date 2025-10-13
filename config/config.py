import re

import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters


load_dotenv()


# Get it from my.telegram.org

API_ID = int(getenv("API_ID", "25092524"))
API_HASH = getenv("API_HASH", "7b14928f710a3992e87e665be40fa6c0")


## Get it from @Botfather in Telegram
BOT_TOKEN = getenv("7714224903:AAEI8X6z_A34C5mDlOQcCaTXBkKnp5Q0uTs")


# Database to save your chats and stats... Get MongoDB:-  https://telegra.ph/How-To-get-Mongodb-URI-04-06
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://aseppp:aseppp@cluster0.bocyf5q.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")


BOT_USERNAME = getenv("@SeppMusikk_bot")


CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "5")
)  # Remember to give value in Seconds


# Custom max audio(music) duration for voice chat. set DURATION_LIMIT in variables with your own time(mins), Default to 60 mins.
DURATION_LIMIT_MIN = int(
    getenv("DURATION_LIMIT", "50000")
)  # Remember to give value in Minutes

# forced entry
MUST_JOIN = getenv("MUST_JOIN")


EXTRA_PLUGINS = getenv(
    "EXTRA_PLUGINS",
    "True",
)

# Fill True if you want to load extra plugins


EXTRA_PLUGINS_REPO = getenv(
    "EXTRA_PLUGINS_REPO",
    "https://github.com/Youghsie/yanto.git",
)
# Fill here the external plugins repo where plugins that you want to load


EXTRA_PLUGINS_FOLDER = getenv("EXTRA_PLUGINS_FOLDER", "plugins")

# Your folder name in your extra plugins repo where all plugins stored


# Duration Limit for downloading Songs in MP3 or MP4 format from bot
SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "500")
)  # Remember to give value in Minutes


# You'll need a Private Group ID for this.
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1002693386777"))


# Your User ID.
OWNER_ID = list(
    map(int, getenv("OWNER_ID", "7931457261").split())
)  # Input type must be interger


# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

# You have to Enter the app name which you gave to identify your  Music Bot in Heroku.
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")


# For customized or modified Repository
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/AayAzhar14/Alphaaa.git",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")

# GIT TOKEN ( if your edited repo is private)
GIT_TOKEN = getenv(
    "GIT_TOKEN")


# Only  Links formats are  accepted for this Var value.
SUPPORT_CHANNEL = getenv(
    "SUPPORT_CHANNEL", "https://t.me/awdfilm"
)  # Example:- https://t.me/TheTeamVivek
SUPPORT_GROUP = getenv(
    "SUPPORT_GROUP", "https://t.me/aseppppv"
)  # Example:- https://t.me/TheTeamVk


# Set it in True if you want to leave your assistant after a certain amount of time. [Set time via AUTO_LEAVE_ASSISTANT_TIME]
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", False)

# Time after which you're assistant account will leave chats automatically.
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "50000")
)  # Remember to give value in Seconds

# mode PRIVATE
PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", "False")


# Time sleep duration For Youtube Downloader
YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "3"))

# Time sleep duration For Telegram Downloader
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "5"))


# Your Github Repo.. Will be shown on /start Command
GITHUB_REPO = getenv("GITHUB_REPO", "https://t.me/aseppppv")


# Spotify Client.. Get it from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "19609edb1b9f4ed7be0c8c1342039362")
SPOTIFY_CLIENT_SECRET = getenv(
    "SPOTIFY_CLIENT_SECRET", "409e31d3ddd64af08cfcc3b0f064fcbe"
)


# Maximum number of video calls allowed on bot. You can later set it via /set_video_limit on telegram
VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "5"))


# Maximum Limit Allowed for users to save playlists on bot's server
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))

# MaximuM limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))


# Telegram audio  and video file size limit

TG_AUDIO_FILESIZE_LIMIT = int(
    getenv("TG_AUDIO_FILESIZE_LIMIT", "1048574951424")
)  # Remember to give value in bytes

TG_VIDEO_FILESIZE_LIMIT = int(
    getenv("TG_VIDEO_FILESIZE_LIMIT", "1048574951424")
)  # Remember to give value in bytes

SET_CMDS = getenv("SET_CMDS", "False")

STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

# ops
BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "Rynlogs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []


# Images
PHOTO = list(
    filter(
        None,
        getenv("PHOTO_LINKS", "https://files.catbox.moe/82oza5.jpeg").split(),
    )
)


START_IMG_URL = getenv(
    "START_IMG_URL",
    "https://files.catbox.moe/82oza5.jpeg",
)
PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://files.catbox.moe/82oza5.jpeg",
)

PLAYLIST_IMG_URL = getenv(
    "PLAYLIST_IMG_URL",
    "https://files.catbox.moe/82oza5.jpeg",
)

GLOBAL_IMG_URL = getenv(
    "GLOBAL_IMG_URL",
    "https://files.catbox.moe/82oza5.jpeg",
)

STATS_IMG_URL = getenv(
    "STATS_IMG_URL",
    "https://files.catbox.moe/82oza5.jpeg",
)

TELEGRAM_AUDIO_URL = getenv(
    "TELEGRAM_AUDIO_URL",
    "https://files.catbox.moe/82oza5.jpeg",
)

TELEGRAM_VIDEO_URL = getenv(
    "TELEGRAM_VIDEO_URL",
    "https://files.catbox.moe/82oza5.jpeg",
)

STREAM_IMG_URL = getenv(
    "STREAM_IMG_URL",
    "https://files.catbox.moe/82oza5.jpeg",
)

SOUNCLOUD_IMG_URL = getenv(
    "SOUNCLOUD_IMG_URL",
    "https://files.catbox.moe/82oza5.jpeg",
)

YOUTUBE_IMG_URL = getenv(
    "YOUTUBE_IMG_URL",
    "https://files.catbox.moe/82oza5.jpeg",
)

SPOTIFY_ARTIST_IMG_URL = getenv(
    "SPOTIFY_ARTIST_IMG_URL",
    "https://files.catbox.moe/82oza5.jpeg",
)

SPOTIFY_ALBUM_IMG_URL = getenv(
    "SPOTIFY_ALBUM_IMG_URL",
    "https://files.catbox.moe/82oza5.jpeg",
)

SPOTIFY_PLAYLIST_IMG_URL = getenv(
    "SPOTIFY_PLAYLIST_IMG_URL",
    "https://files.catbox.moe/82oza5.jpeg",
)


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        print(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        print(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if GITHUB_REPO:
    if not re.match("(?:http|https)://", GITHUB_REPO):
        print(
            "[ERROR] - Your GITHUB_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()


if PING_IMG_URL:
    if PING_IMG_URL != "https://files.catbox.moe/82oza5.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            print(
                "[ERROR] - Your PING_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if PLAYLIST_IMG_URL:
    if PLAYLIST_IMG_URL != "https://files.catbox.moe/82oza5.jpeg":
        if not re.match("(?:http|https)://", PLAYLIST_IMG_URL):
            print(
                "[ERROR] - Your PLAYLIST_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if GLOBAL_IMG_URL:
    if GLOBAL_IMG_URL != "https://files.catbox.moe/82oza5.jpeg":
        if not re.match("(?:http|https)://", GLOBAL_IMG_URL):
            print(
                "[ERROR] - Your GLOBAL_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if STATS_IMG_URL:
    if STATS_IMG_URL != "https://files.catbox.moe/82oza5.jpeg":
        if not re.match("(?:http|https)://", STATS_IMG_URL):
            print(
                "[ERROR] - Your STATS_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if TELEGRAM_AUDIO_URL:
    if TELEGRAM_AUDIO_URL != "https://files.catbox.moe/82oza5.jpeg":
        if not re.match("(?:http|https)://", TELEGRAM_AUDIO_URL):
            print(
                "[ERROR] - Your TELEGRAM_AUDIO_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if STREAM_IMG_URL:
    if STREAM_IMG_URL != "https://files.catbox.moe/82oza5.jpeg":
        if not re.match("(?:http|https)://", STREAM_IMG_URL):
            print(
                "[ERROR] - Your STREAM_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if SOUNCLOUD_IMG_URL:
    if SOUNCLOUD_IMG_URL != "https://files.catbox.moe/82oza5.jpeg":
        if not re.match("(?:http|https)://", SOUNCLOUD_IMG_URL):
            print(
                "[ERROR] - Your SOUNCLOUD_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if YOUTUBE_IMG_URL:
    if YOUTUBE_IMG_URL != "https://files.catbox.moe/82oza5.jpeg":
        if not re.match("(?:http|https)://", YOUTUBE_IMG_URL):
            print(
                "[ERROR] - Your YOUTUBE_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if TELEGRAM_VIDEO_URL:
    if TELEGRAM_VIDEO_URL != "https://files.catbox.moe/82oza5.jpeg":
        if not re.match("(?:http|https)://", TELEGRAM_VIDEO_URL):
            print(
                "[ERROR] - Your TELEGRAM_VIDEO_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()
