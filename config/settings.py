"""Application configuration
 this module loads environment variables from the .env file 
 and exposes them to the rest of the application."""

import os

from dotenv import load_dotenv

#Load environment variables from .env
load_dotenv()

# -----------------------------
# Wazuh API Configuration
# -----------------------------

WAZUH_URL = os.getenv("WAZUH_URL")
WAZUH_USERNAME = os.getenv("WAZUH_USERNAME")
WAZUH_PASSWORD = os.getenv("WAZUH_PASSWORD")

VERIFY_SSL = os.getenv("VERIFY_SSL","False").lower()=="true"

# -----------------------------
# Validation
# -----------------------------

required_settings = {
    "WAZUH_URL" : WAZUH_URL,
    "WAZUH_USERNAME" : WAZUH_USERNAME,
    "WAZUH_PASSWORD" : WAZUH_PASSWORD,
}

missing = [key for key, value in required_settings.items() if not value] 

if missing:
    raise ValueError(
        f"Missing required environment variables: {', '.join(missing)}"
    )


# -----------------------------
# Indexer API Configuration
# -----------------------------

INDEXER_URL = os.getenv("INDEXER_URL")
INDEXER_USERNAME = os.getenv("INDEXER_USERNAME")
INDEXER_PASSWORD = os.getenv("INDEXER_PASSWORD")

VERIFY_SSL = os.getenv("VERIFY_SSL","False").lower()=="true"