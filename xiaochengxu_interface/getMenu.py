import requests
import json
import time

def get_menu():
    headers = {"qrxs-version": "6301", "charset": "utf-8", "qrxs-from": "xcx", "qrxs-token": "89359QJWfaDAA6ChkqMr8s1FGdAfaHXnJEfOA1KHBy46cVnFVjsUs4/yDKOacg", "qrxs-appid": "10001",
               "content-type": "application/json", "qrxs-sex": "2", "qrxs-channel": "90001"}
    url = "https://test-h5.zibingwl.com/xcx4/homeStyle/getMenu?time_stamp=1622623037&nonce_str=ZCbQymmKnBW28HxQKNJb&api_sign=1FD8CC016181E8DDF9E7F5A32F1909B0"
    start_time = int(time.time()*1000)
    # print(start_time)
    re = requests.get(headers=headers, url=url)
    end_time = int(time.time()*1000)
    # print(end_time)
    consume_time = end_time - start_time
    # print(consume_time)
    # print(re.status_code)
    # print(re.text)
    # json.loads(re.text)['status']
    return [re.status_code, consume_time]



