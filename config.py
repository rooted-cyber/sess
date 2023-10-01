from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = 3704772
API_HASH = "b8e50a035abb851c0dd424e14cac4c06"

BOT_TOKEN = getenv("BOT_TOKEN")
OWNER_ID = int(getenv("OWNER_ID"))

MONGO_DB_URI = getenv("MONGO_DB_URI")
MUST_JOIN = getenv("MUST_JOIN", None)
