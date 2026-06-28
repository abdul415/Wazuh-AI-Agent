from dataclasses import dataclass, field
from typing import Any

@dataclass
class Alert:
    """Represents a Wazuh security alert."""

    alert_id: str
    timestamp: str

    agent_id: str
    agent_name: str
    agent_ip: str

    rule_id: str
    rule_level: str
    rule_description: str

    groups: list[str]

    location: str

    raw_data: dict[str, Any] = field(repr=False)