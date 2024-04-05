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
BOT_TOKEN = environ.get("BOT_TOKEN", "6380624575:AAEOLrpHS0eVcWcgGTuJm33fzeAMoDeJeIc")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1001973960964"))
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
OPENAI_API_KEY = environ.get('OPENAI_API_KEY', "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")
#Openai
AI = is_enabled((environ.get("AI","True")), True)
OPENAI_API = environ.get("OPENAI_API", " ")
DEEP_API = environ.get("DEEP_API", "3ac9b077-654f-45c6-a1f0-a04a5ef6b69e")
GOOGLE_API_KEY = environ.get("GOOGLE_API_KEY", "AIzaSyD214hhYJ-xf8rfaWX044_g1VEBQ0ua55Q")
AI_LOGS = int(environ.get("AI_LOGS", "-1002028053413")) #GIVE YOUR NEW LOG CHANNEL ID TO STORE MESSAGES THAT THEY SEARCH IN BOT PM.... [ i have added this to keep an eye on the users message, to avoid misuse of Bot ]
BOT_USERNAME = environ.get("BOT_USERNAME", "YD_2GPT_BOT")
