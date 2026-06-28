from config.settings import(
    WAZUH_PASSWORD,
    WAZUH_URL,
    WAZUH_USERNAME,
    VERFIY_SSL,
)

print("Wazuh URL:",WAZUH_URL)
print("Username:",WAZUH_USERNAME)
print("Password:","*" * len(WAZUH_PASSWORD))
print("Verify SSL:",VERFIY_SSL)