import requests
import time

url = "http://57.129.135.89:1337/receive_player_data"
data = {
    "playerName": "@everyone @here fucked by @spookyaysaa dm for a better rat LOL"
}
headers = {
    "Content-Type": "application/json"
}

while True:
    r = requests.post(url, json=data, headers=headers)
    print(f"Status: {r.status_code}")
    print(f"Response: {r.text}")
    time.sleep(30)
