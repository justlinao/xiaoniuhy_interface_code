import requests


def xunzhang():
    headers = {
        'device-brand': 'huawei',
        'request-id': '948f1b52-e3f5-45e0-9d8b-333a325e8f48',
        'language': 'cn',
        'request-agent': '1',
        'device-id': 869275041739234,
        'os-version': '0',
        'sdk-version': '29',
        'phone-model': 'TAS-AL00',
        'market': 'fyclean_hellogeek_test',
        'app-version': '1.1.1_dev',
        'app-version-code': '12',
        'app-name': 'fy_clean',
        'app-id': '184001',
        'timestamp': '1606727662245',
        'sign': '38E2B839A9761D2C49CE102B570F7640CED1BBDDB05ABECB15C1AE1ED0FD0E45',
        'customer-id': '783024540627267590',
        'access-token': '782973118082711610',
        'sm-deviceid': '202005271554387fccd35998989ff69d037ba639b276cd0153e857339eb594',
        'sdk-uid': 'e2525ea5b0a0d4c8_feebbeed-f5e7-8dcb-6fc7-fef6b6f6f44f',
        'activate-timestamp': '1606716817',
        'Content-Type': 'application/json; charset=utf-8',
        'Content-Length': 17,
        'Host': 'fat-clesystem.mloveli.com',
        'Accept-Encoding': 'gzip',
    }
    url = "http://fyjsclesystem.mloveli.com/medal/user/configs"
    data = {}
    re = requests.get(url, headers)
    print(re.text)


xunzhang()
