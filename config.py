from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "8260758"))
API_HASH = getenv("API_HASH", "f1978dac0dafe758700fac54d207b26f")
BOT_TOKEN = getenv("BOT_TOKEN","5192831405:AAGxZq9Iu7Y73GgDK-y5aknGXp27x6jNI38")
BOT_NAME = getenv("BOT_NAME","Itscrazy2_bot")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "120"))
SESSION_NAME = getenv("SESSION_NAME")
MASTER_USERNAME = list(getenv("MASTER_USERNAME", "MASOOM_LOVER_BOT"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5373329232 5450805606 5545626276 5533277204 5334643009").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "FULL_ON_MOJJ_MASTI")
