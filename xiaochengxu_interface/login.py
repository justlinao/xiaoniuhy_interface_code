# -*- coding: UTF-8 -*-
import json
import requests
from Public.response_time import res_time

"""
登录接口
"""


@res_time
def get_login():
    headers = {"qrxs-version": "6301", "charset": "utf-8", "qrxs-from": "xcx", "qrxs-token": "56edOAMIGH8TuSUjONWcUDbG8PQ/3xpdjB4AWhwJQ4/O8o249EE5f/6uuAqpLxymqRRPPfU", "qrxs-appid": "10001",
               "content-type": "application/json", "qrxs-sex": "2", "qrxs-channel": "90001"}
    url = "https://wxmini.shruisong.net/xcx4/login/wxmini_login_full.html?code=051PIzFa1qFmbB0AhOIa1cozV53PIzF5&appid=10001&time_stamp=1623153095&nonce_str=TbmRz6XaR3edrtzFhX3W&api_sign=104878ACB8F05F35F951F4F9137A9DF5"
    re = requests.get(headers=headers, url=url)
    # print(re.status_code)
    # print(json.loads(re.text))
    # json.loads(re.text)['status']
    return re.status_code


get_login()
