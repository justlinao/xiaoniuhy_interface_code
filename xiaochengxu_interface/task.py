# -*- coding: UTF-8 -*-
import requests
from Public.response_time import res_time

"""
优惠券任务
"""


@res_time
def get_task():
    headers = {"qrxs-version": "6301", "charset": "utf-8", "qrxs-from": "xcx",
               "qrxs-token": "89359QJWfaDAA6ChkqMr8s1FGdAfaHXnJEfOA1KHBy46cVnFVjsUs4/yDKOacg", "qrxs-appid": "10001",
               "content-type": "application/json", "qrxs-sex": "2", "qrxs-channel": "90001"}
    url = "https://wxmini.shruisong.net/xcx4/coupon/task?type=4&time_stamp=1623153095&nonce_str=QcQ3isnGTTEDrhyMZMRj&api_sign=A5A0436F00D3055C54988695E3BC155F"
    re = requests.get(headers=headers, url=url)
    # print(re.status_code)
    # print(re.text)
    # json.loads(re.text)['status']
    return re.status_code