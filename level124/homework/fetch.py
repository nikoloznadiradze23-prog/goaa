import requests

url = ""
response = requests.get(url)
data = response.json()
print("name:", data["name"])
print("Owner:", data["owner"]["login"])
print("Description:", data["description"])
