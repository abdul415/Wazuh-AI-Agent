# from config.settings import(
#     WAZUH_PASSWORD,
#     WAZUH_URL,
#     WAZUH_USERNAME,
#     VERFIY_SSL,
# )

# print("Wazuh URL:",WAZUH_URL)
# print("Username:",WAZUH_USERNAME)
# print("Password:","*" * len(WAZUH_PASSWORD))
# print("Verify SSL:",VERFIY_SSL)


from tools.wazuh_api import WazuhAPI

wazuh = WazuhAPI()

# print("Basee URL:",wazuh.base_url)
# print("Username:",wazuh.username)
# print("Verfy SSL:",wazuh.verify_ssl)
# print("Session:",wazuh.session)
# print("Token:",wazuh.token)

# try:
#     wazuh.authenticate()

#     print("Authentication successful!")
#     print()
#     print("Token:")
#     print(wazuh.token[:50] + "...")

# except Exception as e:
#     print("Authentication failed!")
#     print(e)

try: 
    wazuh.authenticate()

    info = wazuh._request(
        "GET",
        "/manager/info"
    )

    print(info) 
    
except Exception as e:
    print(e)