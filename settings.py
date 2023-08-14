import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")
VERIFY_CHANNEL_TOKEN = int(os.environ["VERIFY_CHANNEL"])
WELCOME_CHANNEL_TOKEN = int(os.environ["WELCOME_CHANNEL"])