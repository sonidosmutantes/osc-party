import requests

# Create server instance
url = "http://localhost:5010/filter"

headers = {
    'from': "127.0.0.1",
    'to': "127.0.0.1",
    'addr': "*",
    'type': "f",
    'motor': "2",
    'authorization': "Token",
    'cache-control': "no-cache",
    'postman-token': "65cda486-a2bf-0304-cdc5-2392b57dda5c"
    }

response = requests.request("POST", url, headers=headers)

print(response.text)


# Set up connections
url = "http://localhost:5010/filter"

# Motor 1
headers = {
    'from': "127.0.0.1",
    'to': "127.0.0.1",
    'addr': "*",
    'type': "f",
    'motor': "1",
    'authorization': "Token",
    }

response = requests.request("POST", url, headers=headers)

print(response.text)

# Motor 2
headers = {
    'from': "127.0.0.1",
    'to': "127.0.0.1",
    'addr': "*",
    'type': "f",
    'motor': "2",
    'authorization': "Token",
    }

response = requests.request("POST", url, headers=headers)

print(response.text)
