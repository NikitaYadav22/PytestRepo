import json
import posixpath
import urllib
import requests
import os
import time

class Parm():
    with open('params.json', 'r') as data:
        data = json.load(data)
        url = data["parm_url"]
        headers = data["parm_headers"]
    
    def __init__(self):
        digital_id = os.environ.get('DIGITAL_ID')
        self.url = posixpath.join(self.url, digital_id)

    def get_parm(self):
        time.sleep(20)
        response = requests.request("GET", self.url, headers=self.headers)
        print("PARM url = ",self.url)
        print("Response = ", response.text)
        return response
