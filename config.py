import  os

BOT_TOKEN = os.environ.get("BOT_TOKEN")
APP_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
youtube_next_fetch = 0 
EDIT_TIME = 5
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())
DB_URL = os.environ.get("DB_URL", "")
DB_NAME = os.environ.get("DB_NAME", "BroadcastBot")
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
LOG_CHNL = int(os.environ.get("LOG_CHANNEL", ""))
USE_HEROKU = os.environ.get("USE_HEROKU", "True")
