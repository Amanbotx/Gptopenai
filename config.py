import re
from os import getenv, environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

API_ID = int(environ.get("API_ID", "24004349"))
API_HASH = environ.get("API_HASH", "5aabfb11c262b17d568d828a3100f296")
BOT_TOKEN = environ.get("BOT_TOKEN", "6883904115:AAFzjOFjf30iab7YEh5dMQ5Y1D0V-6bBQ74")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002062708890"))
ADMINS = int(environ.get("ADMINS", "5977931010"))
DB_URI = environ.get("DB_URI", "mongodb+srv://ranjuvishwakarma50:aman@cluster0.jfl45jq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = environ.get("DB_NAME", "Cluster0")
OPENAI_API = environ.get("OPENAI_API", "")
AI = is_enabled((environ.get("AI","True")), False)
support_chat_id = environ.get('SUPPORT_CHAT_ID', '-1002028053413')
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
#ask 
GOOGLE_API_KEY = environ.get('API_KEY', 'AIzaSyASKXFxSjnvHO_k5kibkqf8DOdLjh9G4Hs')
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'https://t.me/Amanchatgroup1')
