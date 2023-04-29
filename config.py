from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "13615830"))
API_HASH = getenv("API_HASH", "9c480c327878c224bda99853f5541652")
BOT_TOKEN = getenv("BOT_TOKEN", None)
BOT_NAME = getenv("BOT_NAME", "KNAYA")
BOT_USERNAME = getenv("BOT_USERNAME", "KNAYA_MUSIC_BOT")
OWNER_USERNAME = getenv("OWNER_USERNAME", "its_Coder_xD")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "ARCH_SUPPORTS")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
START_IMG = getenv("START_IMG", "https://graph.org/file/1e151cf9b0afd0aff05a4.jpg")
PING_IMG = getenv("PING_IMG", "https://graph.org/file/55b52e5b79e3e542f1233.jpg")
SESSION_NAME = getenv("SESSION_NAME", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "? ~ + • / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5856908645").split()))
