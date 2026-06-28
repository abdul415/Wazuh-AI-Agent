""" 
Wazuh API Client

Responsible for:
-Connecting to the Wazuh API
-Authenticating
-Managing the authentication token
"""

import requests

from config.settings import(
    WAZUH_PASSWORD,
    WAZUH_URL,
    WAZUH_USERNAME,
    VERFIY_SSL,
)

class WazuhAPI:
    """ Client for interacting with the Wazuh REST API."""

    def __init__(self):
        self.base_url = WAZUH_URL
        self.username = WAZUH_USERNAME
        self.passowrd = WAZUH_PASSWORD
        self.verify_ssl = VERFIY_SSL

        #Reuse HTTP connections
        self.session = requests.Session()

        #JWT token will be stored here after authentication
        self.token = None

        #timeout
        self.timeout = 30