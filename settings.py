import os
import pathlib
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")

BASE_DIR = pathlib.Path(__file__).parent

CMDS_DIR = BASE_DIR / "cmds"
COGS_DIR = BASE_DIR / "cogs"