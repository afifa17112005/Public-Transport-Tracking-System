import time
import random
import requests

URL = "http://127.0.0.1:5000/update_location"

bus_ids = ["Bus-1", "Bus-2", "Bus-3"]

while True:
    for bus_id in bus_ids:
        latitude = 12.9716 + random.uniform(-0.01, 0.01)
        longitude = 77.5946 + random.uniform(-0.01, 0.01)
        data = {
            "bus_id": bus_id,
            "latitude": latitude,
            "longitude": longitude
        }
        try:
            requests.post(URL, json=data)
        except:
            pass
    time.sleep(5)
