import pytest
import os
import pandas
import json

from requests import request
from Utils import Order, Payment, Digital, Parm, Checkin

def plus():
    excel_data_df = pandas.read_excel('tes_excel.xlsx', sheet_name='Sheet1')
    mylist = excel_data_df['PLU'].tolist()
    return mylist

@pytest.fixture(scope='session', params=plus())
def generate_payload(request):
    with open("payload_sample.json", "r") as outfile:
        json_object = json.load(outfile)
    json_object['items'][0]['product_id'] = request.param
    yield json.dumps(json_object)

class TestAPI:
  def test_successful_order(self, generate_payload):
    order = Order.Order()
    gen_order = order.generate_order(generate_payload)
    order.set_order_id(gen_order)
    assert gen_order.status_code == 200

  def test_successful_payment(self, generate_payload):
    payment = Payment.Payment()
    make_payment = payment.make_payment()
    assert make_payment.status_code == 200

  # def test_commit_payment(self,generate_payload):
  #   payment = Payment.Payment()
  #   commit_payment = payment.commit_payment()
  #   assert commit_payment.status_code == 200

  # def test_digital_id(self,generate_payload):
  #   digital = Digital.Digital()
  #   digital_resp = digital.digtal_id()
  #   assert digital_resp.status_code == 200

  # @pytest.mark.dependency(name='test_parm')
  # def test_parm(self,generate_payload):
  #   parm = Parm.Parm()
  #   parm_resp = parm.get_parm()
  #   assert parm_resp.status_code == 202
  #   print(parm_resp.status_code)
  #   parm_resp = parm_resp.json()
  #   assert parm_resp['order_status'] == 'POS_RECEIVED'

  # @pytest.mark.dependency(depends=['test_parm'])
  # def test_checkin(self,generate_payload):
  #   checkin = Checkin.Checkin()
  #   checkin_resp = checkin.checkin()
  #   assert checkin_resp.status_code == 200

@pytest.fixture(scope='session', autouse=True)
def cleanup(request):
    print("Cleanup environment variables once we are finished.")
    def clean_env_variables():
        os.unsetenv("ORDER_ID")
        os.unsetenv("DIGITAL_ID")
    request.addfinalizer(clean_env_variables)


