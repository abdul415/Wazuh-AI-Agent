"""Indexer API Client

Responsible for retrieving alerts from Wazuh Indexer.
"""

import requests
import urllib3
from models.alert import Alert

from config.settings import (
    INDEXER_URL,
    INDEXER_PASSWORD,
    INDEXER_USERNAME,
    VERIFY_SSL,
)

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class IndexerAPI:
    def __init__(self):
        
        self.base_url = INDEXER_URL
        self.username = INDEXER_USERNAME
        self.password = INDEXER_PASSWORD
        self.verify_ssl = VERIFY_SSL

        self.session = requests.Session()

        self.session.auth = (

            self.username,
            self.password,
        )

        self.timeout = 30
    
    def _search(self, index, query):

        response = self.session.post(
            f"{self.base_url}/{index}/_search",
            json = query,
            verify=self.verify_ssl,
            timeout=self.timeout,
        )

        response.raise_for_status()

        return response.json()
    
    def get_latest_alerts(self, limit: int=10):
        """
        Retreive the latest alerts from the Wazuh Indexer
        """
        query = {
            "size":limit,
            "sort": [
                {
                    "@timestamp":{
                        "order":"desc"
                    }
                }
            ]
        }

        result = self._search(
            "wazuh-alerts-4.x-*",
            query,
        )

        alerts = []

        hits = result["hits"]["hits"]

        for hit in hits:
            source = hit["_source"]

            alert = Alert(
                alert_id=source.get("id", ""),
                timestamp=source.get("timestamp", ""),

                agent_id=source.get("agent",{}).get("id", ""),
                agent_name = source.get("agent",{}).get("name", ""),
                agent_ip=source.get("agent",{}).get("ip", ""),

                rule_id = source.get("rule",{}).get("id", ""),
                rule_level = source.get("rule",{}).get("level", 0),
                rule_description = source.get("rule",{}).get("description", ""),

                groups = source.get("rule", {}).get("groups", []),

                location=source.get("location", ""),

                raw_data=source,
            )

            alerts.append(alert)

        return alerts