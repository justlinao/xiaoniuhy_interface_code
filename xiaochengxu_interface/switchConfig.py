# -*- coding: UTF-8 -*-
import json
import requests
from Public.response_time import res_time

"""
登录接口
"""


@res_time
def get_switch_config():
    headers = {"qrxs-version": "6301", "charset": "utf-8", "qrxs-from": "xcx", "qrxs-token": "56edOAMIGH8TuSUjONWcUDbG8PQ/3xpdjB4AWhwJQ4/O8o249EE5f/6uuAqpLxymqRRPPfU", "qrxs-appid": "10001",
               "content-type": "application/json", "qrxs-sex": "2", "qrxs-channel": "90001"}
    url = "https://wxmini.shruisong.net/xcx4/app/switch_config?interface_version=4&time_stamp=1623153096&nonce_str=ErAwdQ7h2bdBj8T4B7rN&api_sign=0E6C8540A3A3308DF816FBB9E2773CC7"
    re = requests.get(headers=headers, url=url)
    # print(re.status_code)
    # print(json.loads(re.text))
    # json.loads(re.text)['status']
    return re.status_code


get_switch_config()
