import os
from dotenv import load_dotenv

load_dotenv()

API_TIMEOUT = int(os.getenv("API_TIMEOUT", "30"))
REFRESH_INTERVAL = int(os.getenv("REFRESH_INTERVAL", "60"))
DEBUG_MODE = os.getenv("DEBUG_MODE", "False").lower() == "true"

SUPPORTED_CRYPTOS = [
    "bitcoin",
    "ethereum", 
    "dogecoin",
    "cardano",
    "polkadot"
]

DEFAULT_CURRENCY = "usd"