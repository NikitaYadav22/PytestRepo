import json
import requests
import os
import pytest
import pandas



class Order():
    with open('params.json', 'r') as data:
        data = json.load(data)
        url = data["url"]
        headers = data["headers"]

    def set_order_id(self, response):
            response_data = response.json()
            order_id=response_data['order']['_id']
            os.environ['ORDER_ID']= order_id
            return True

    def generate_order(self, generate_payload):
        response = requests.request("POST", self.url, headers=self.headers, data=generate_payload)
        print("Order url = ", self.url)
        print("Response = ", response.text)
        self.set_order_id(response)
        return response