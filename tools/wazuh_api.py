""" 
Wazuh API Client

Responsible for:
-Connecting to the Wazuh API
-Authenticating
-Managing the authentication token
"""

import requests
from requests.auth import HTTPBasicAuth

from config.settings import(
    WAZUH_PASSWORD,
    WAZUH_URL,
    WAZUH_USERNAME,
    VERIFY_SSL,
)

class WazuhAPI:
    """ Client for interacting with the Wazuh REST API."""

    def __init__(self):
        self.base_url = WAZUH_URL
        self.username = WAZUH_USERNAME
        self.password = WAZUH_PASSWORD
        self.verify_ssl = VERIFY_SSL

        #Reuse HTTP connections
        self.session = requests.Session()

        #JWT token will be stored here after authentication
        self.token = None

        #timeout
        self.timeout = 30

    def authenticate(self):
        """
        Authenticate with the Wazuh API and store the JWT token.
        """

        endpoint = f"{self.base_url}/security/user/authenticate?raw=true"

        response = self.session.post(
            endpoint,
            auth = HTTPBasicAuth(self.username, self.password),
            verify=self.verify_ssl,
            timeout=self.timeout,
        )

        response.raise_for_status()

        self.token = response.text

        self.session.headers.update({
            "Authorization":f"Bearer {self.token}"
        })

        return True

    def _request(self, method, endpoint, **kwargs):
        """ 
        Internal helper for making authenticated API requests.
        """

        url = f"{self.base_url}{endpoint}"

        response = self.session.request(
            method=method,
            url=url,
            verify=self.verify_ssl,
            timeout=self.timeout,
            **kwargs
        )

        response.raise_for_status()

        return response.json()