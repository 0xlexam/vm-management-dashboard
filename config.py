import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY", "Your_Default_API_Key")

DATABASE = {
    'NAME': os.getenv("DB_NAME", "default_db_name"),
    'USER': os.getenv("DB_USER", "default_user"),
    'PASSWORD': os.getenv("DB_PASSWORD", "default_password"),
    'HOST': os.getenv("DB_HOST", "localhost"),
    'PORT': int(os.getenv("DB_PORT", 5432)),
}

DEBUG_MODE = os.getenv("DEBUG_MODE", "False").lower() in ('true', '1', 't')
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")