from os import getenv, environ
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
TOKEN = getenv("TOKEN")
VERIFY_CHANNEL_TOKEN = int(environ["VERIFY_CHANNEL"])
WELCOME_CHANNEL_TOKEN = int(environ["WELCOME_CHANNEL"])
ANON_CHANNEL_TOKEN = int(environ["ANON_CHANNEL"])
VERIFY_MESSAGE_ID = None
ANON_MESSAGE_ID = None

# DIRECTORIES
BASE_DIR = Path(__file__).parent
LOGS_DIR = BASE_DIR / "logs"
