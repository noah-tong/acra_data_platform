from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

ROOT_DIR = Path(__file__).resolve().parent.parent

BRONZE_PATH = ROOT_DIR / "bronze"
LOG_PATH = ROOT_DIR / "logs"

AERODATABOX_API_KEY = os.getenv("AERODATABOX_API_KEY")
EIA_API_KEY = os.getenv("EIA_API_KEY")

BASE_URL = "http://api.aviationstack.com/v1"

REQUEST_TIMEOUT = 60

MAX_RETRY = 3

RETRY_BACKOFF = 2

MAX_WORKERS = 5

PAGE_LIMIT = 100