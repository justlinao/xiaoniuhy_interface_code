# -*- coding: UTF-8 -*-
from Public.db import *
import time
import hmac
import hashlib
import requests
import json
timestamp = str(int(time.time()))
appId = '1149960309183299584'   # 1149960309183299584
key = appId + str(timestamp)
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


def eggsmash():
    header = {
        "request-id": "7B142B65-A3A4-4F63-8C90-50FB9ADB6817-1590994839806",
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
        "customer-id": 'c3d69445835d4fc2b52903321cfda555',
        "access-token": '11d2fc73aac546d19c8d374d9f3a9220',
        "gps-lng": "23.26",
        "gps-lat": "23.26",
        "Content-Type": "application/json;charset=utf-8",
        # "Content-Type": "application/x-www-form-urlencoded"
    }
    url = 'http://qx-fat.qianshi188.com/gateway/activity/smashEggsAward/eggSmashSubmit'
    data = {'hammerNum': 66, 'roomId': '001378578bd044778579a7dda9d45cdc', 'isAllLook': '2'}
    re = requests.post(url=url, headers=header, data=json.dumps(data))
    print(re.text)


while True:
    eggsmash()
