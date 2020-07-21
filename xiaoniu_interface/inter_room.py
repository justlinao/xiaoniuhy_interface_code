# -*- coding: UTF-8 -*-
import time
import hmac
import hashlib
import requests
import json
from Public.db import DB
import base64
'''
不同端对应的 app-id，app-secret
api.security.app.account-config.[android-1].app-id = 1149954699146534912
api.security.app.account-config.[android-1].app-secret = 16a9cc89a54511e993fc506b4bbe1bc4
api.security.app.account-config.[ios-1].app-id = 1149960309183299584
api.security.app.account-config.[ios-1].app-secret = 1acdf792a54511e993fc506b4bbe1bc4
api.security.app.account-config.[h5-1].app-id = 1149961032218419200
api.security.app.account-config.[h5-1].app-secret = 20c923b2a54511e993fc506b4bbe1bc4
'''

timestamp = str(int(time.time()))
appId = '1149960309183299584'
key = appId+str(timestamp)
appSecret = '1acdf792a54511e993fc506b4bbe1bc4'


def hmac_sha256(key, appSecret):
    """
    hmacsha256加密
    return:加密结果转成16进制字符串形式
    """
    appSecret = appSecret.encode('UTF-8')
    key = key.encode('UTF-8')
    sign = hmac.new(appSecret, key, digestmod=hashlib.sha256).hexdigest()
    sign.encode()
    # print(sign.upper())
    return sign.upper()


class Test(DB):
    def test_query(self):
        re = DB.query_db(self,
                     "SELECT customer_id FROM qx_live_customer_test.customer LIMIT 100")
        print(re)
        return re


def interroom():
    for i in Test().test_query():
        header = {
            "request-id": "142B65-A3A4-4F63-8C90-50FB9ADB6817-1590994839806",
            "request-agent": "2",
            "device-id": "A17EFC0B198941CBA693915B5A0B4472",
            "os-version": "1",
            "phone-model": "iPhone11,6",
            "sdk-version": "13.4",
            "market": "app_store",
            "app-version": "1.0.0",
            "app-version-code": "100",
            "app-name": "1",
            "app-clone-name": "001",
            "biz-code": "/gateway/room/liveroom/queryliveroom",
            "app-id": "1149960309183299584",
            "timestamp": timestamp,
            "sign": hmac_sha256(key, appSecret),
            "customer-id": i,
            "access-token": "11d2fc73aac546d19c8d374d9f3a9220",
            "gps-lng": "23.26",
            "gps-lat": "23.26",
            "Content-Type": "application/json;charset=utf-8"
        }
        url = "http://qx-fat.qianshi188.com/gateway/room/liveroom/queryliveroom"
        data = {"customerId": "bb239ae644ec4541bee885bdd1b7b279"}
        re = requests.post(url=url, headers=header, data=json.dumps(data))
        print(re.text)


interroom()
