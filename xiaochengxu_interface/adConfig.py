# -*- coding: UTF-8 -*-
import requests
from Public.response_time import res_time

"""
广告列表值
"""


@res_time
def get_adconfig():
    headers = {"qrxs-version": "6301", "charset": "utf-8", "qrxs-from": "xcx",
               "qrxs-token": "89359QJWfaDAA6ChkqMr8s1FGdAfaHXnJEfOA1KHBy46cVnFVjsUs4/yDKOacg", "qrxs-appid": "10001",
               "content-type": "application/json", "qrxs-sex": "2", "qrxs-channel": "90001"}
    url = "https://wxmini.shruisong.net/xcx4/app/adconfig.html?interface_version=4&time_stamp=1623153096&nonce_str=aMJrYMHPWfKjk762FEJW&api_sign=3C3BEC952B833AF96360054F3B91831A"
    re = requests.get(headers=headers, url=url)
    # print(re.status_code)
    # print(re.text)
    # json.loads(re.text)['status']
    return re.status_code