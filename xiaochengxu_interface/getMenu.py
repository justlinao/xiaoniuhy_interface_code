# -*- coding: UTF-8 -*-
import requests
from Public.response_time import res_time
"""
底部tab接口
"""


@res_time
def get_menu():
    headers = {"qrxs-version": "6301", "charset": "utf-8", "qrxs-from": "xcx", "qrxs-token": "89359QJWfaDAA6ChkqMr8s1FGdAfaHXnJEfOA1KHBy46cVnFVjsUs4/yDKOacg", "qrxs-appid": "10001",
               "content-type": "application/json", "qrxs-sex": "2", "qrxs-channel": "90001"}
    url = "https://wxmini.shruisong.net/xcx4/homeStyle/getMenu?time_stamp=1623153096&nonce_str=rZQndN4sKKDmxkJJEmBY&api_sign=955834823D4A490F5ED59B956BB3EC7C"
    re = requests.get(headers=headers, url=url)
    # print(re.status_code)
    # print(re.text)
    # json.loads(re.text)['status']
    return re.status_code


