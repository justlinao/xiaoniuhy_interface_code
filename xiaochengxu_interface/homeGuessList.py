import requests
import json


def home_guess_list():
    headers = {"qrxs-version": "6301", "charset": "utf-8", "qrxs-from": "xcx", "qrxs-token": "89359QJWfaDAA6ChkqMr8s1FGdAfaHXnJEfOA1KHBy46cVnFVjsUs4/yDKOacg", "qrxs-appid": "10001",
               "content-type": "application/json", "qrxs-sex": "2", "qrxs-channel": "90001"}
    url = "https://test-h5.zibingwl.com/xcx4/homeStyle/homeGuessList?page_index=1&time_stamp=1622623037&nonce_str=2x8XpXaW4dyKjNXck7pk&api_sign=C41F5EE5C41C551F67D94E1C0438E4D2"
    re = requests.get(headers=headers, url=url)
    # print(re.text)
    return json.loads(re.text)['status']