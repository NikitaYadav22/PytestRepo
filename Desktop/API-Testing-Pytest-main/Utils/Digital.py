import json
import posixpath
import urllib
import requests
import os
import time

class Digital():
    payload = json.dumps({
    "reason": "Order has been accepted."
    })
    with open('params.json', 'r') as data:
        data = json.load(data)
        url = data["digital_url"]
        headers = data["digital_headers"]
    
    def __init__(self):
        order_id = os.environ.get('ORDER_ID')
        self.url = posixpath.join(self.url, order_id)

    def digtal_id(self):
        time.sleep(10)
        response = requests.request("GET", self.url, headers=self.headers, data=self.payload)
        print("Get DIGITAL ID url = ",self.url)
        print("Response = ", response.text)
        if response and response.status_code == 200:
            x_id = response.json()['xId']
            os.environ['DIGITAL_ID'] = x_id
        return response
