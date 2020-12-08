import requests
import json


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
        'market': 'fyjsclean_hellogeek_test',
        'app-version': '1.0.1_dev',
        'app-version-code': '2',
        'app-name': 'fyjs_clean',
        'app-id': '181501',
        'timestamp': '1606727662245',
        'sign': '1EAB9DC83B8E25E5DF8CD72F68B7A0BB172B8D6FF6B345F3B6F191332D826F67',
        'customer-id': '783024540627267590',
        'access-token': '783027264919990382',
        'sm-deviceid': '202005271554387fccd35998989ff69d037ba639b276cd0153e857339eb594',
        'sdk-uid': 'd28091f2a5c54fa2_feebbeed-f5e7-8dcb-6fc7-fef6b6f6f44f',
        'activate-timestamp': '1606729169',
        'Content-Type': 'application/json; charset=utf-8',
        'Content-Length': 17,
        'Host': 'dev-jsclesystem.mloveli.com',
        'Accept-Encoding': 'gzip',
    }
    url = "http://dev-jsclesystem.mloveli.com/bubble/collect"
    data = {"userId": "783024540627267590", "locationNum": "2"}
    re = requests.post(url, headers, data)
    print(re.text)


xunzhang()
