import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Retrieve the API key from environment variables or use a default
SERVER_API_KEY = os.getenv("API_KEY", "Your_Default_API_Key")

# Database configuration details, with clearer naming
DATABASE_CONFIG = {
    'NAME': os.getenv("DB_NAME", "default_db_name"),
    'USERNAME': os.getenv("DB_USER", "default_user"),
    'PASSWORD': os.getenv("DB_PASSWORD", "default_password"),
    'HOST_ADDRESS': os.getenv("DB_HOST", "localhost"),
    'PORT_NUMBER': int(os.getenv("DB_PORT", 5432)),
}

# Toggle for enabling or disabling debug mode based on environment variable
IS_DEBUG_MODE_ENABLED = os.getenv("DEBUG_MODE", "False").lower() in ('true', '1', 't')

# Application log level setting
APPLICATION_LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")