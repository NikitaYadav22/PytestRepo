import json
import posixpath
import urllib
import requests
import os

class Checkin():
    payload = json.dumps({
        "destination": {
            "id": "128",
            "name": "Delivery-GH-FC"
        }
    })
    with open('params.json', 'r') as data:
        data = json.load(data)
        url = data["url"]
        headers = data["headers"]
        payment = data["payment"]
    
    def __init__(self):
        order_id = os.environ.get('ORDER_ID')

        checkin_url_path = posixpath.join(order_id, "checkin")
        self.checkin_url=urllib.parse.urljoin(self.url, checkin_url_path)

    def checkin(self):
        response = requests.request("PUT", self.checkin_url, headers=self.headers, data=self.payload)
        print("CHECKIN url = ",self.checkin_url)
        print("Response = ", response.text)
        return response
