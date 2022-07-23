import json
import posixpath
import urllib
import requests
import os
import time

class Payment():
    with open('params.json', 'r') as data:
        data = json.load(data)
        url = data["url"]
        headers = data["headers"]
        payment = data["payment"]
        commit_header = data["commit_header"]
    
    def __init__(self):
        order_id = os.environ.get('ORDER_ID')

        payment_url_path = posixpath.join(order_id, "payment")
        self.payment_url=urllib.parse.urljoin(self.url, payment_url_path)

        commit_url_path = posixpath.join(order_id, "commit")
        self.commit_url=urllib.parse.urljoin(self.url, commit_url_path)

    def make_payment(self):
        response = requests.request("PUT", self.payment_url, headers=self.headers, data=json.dumps(self.payment))
        print("Payment url = ",self.payment_url)
        print("Response = ", response.text)
        return response

    def commit_payment(self):
        time.sleep(3)
        response = requests.request("PUT", self.commit_url, headers=self.commit_header)
        print("Commit url = ",self.commit_url)
        print("Response = ", response.text)
        return response