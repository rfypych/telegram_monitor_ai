import os
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

# Telegram API Credentials
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")

# Session Name (can be anything)
SESSION_NAME = os.getenv("SESSION_NAME", "telegram_monitor_session")

# Target Channels (comma separated in .env)
TARGET_CHANNELS = os.getenv("TARGET_CHANNELS", "").split(",")

# Output file
OUTPUT_FILE = os.getenv("OUTPUT_FILE", "telegram_data.csv")

# Groq AI Configuration
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = os.getenv("GROQ_MODEL", "mixtral-8x7b-32768")

def is_configured():
    """Check if API credentials are provided."""
    return API_ID and API_HASH
