import requests
import time
import random
from datetime import datetime

url = "http://65.38.96.101:8447/login"

payload_template = {
    "content": "@here @everyone ur rat is asscheeks, zsramahi owns u",
    "embeds": [
        {
            "title": "owned fr",
            "description": "better obfuscate next time lmao",
            "color": 16711680,  # Red
            "fields": [
                {"name": "Message", "value": "ur rat is asscheeks @here @everyone, zsramahi owns u", "inline": False}
            ],
            "footer": {"text": "zsr owns you"}
        }
    ]
}

for i in range(150):
    timestamp = datetime.now().strftime("%H:%M:%S")
    try:
        response = requests.post(url, json=payload_template, timeout=5)
        print(f"[{timestamp}] [{i+1}/150] Sent - Status: {response.status_code}")
    except Exception as e:
        print(f"[{timestamp}] [{i+1}/150] Failed - Error: {str(e)}")
    time.sleep(random.uniform(0.1, 0.3))
