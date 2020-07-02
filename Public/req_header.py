import time
import hmac
import hashlib
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
appId = '1149954699146534912'
key = appId+str(timestamp)
appSecret = '16a9cc89a54511e993fc506b4bbe1bc4'


def hmac_sha256(key, appSecret):
    """
    hmacsha256加密
    return:加密结果转成16进制字符串形式
    """
    message = appSecret.encode('utf-8')
    sign = hmac.new(key.encode('utf-8'), message, digestmod=hashlib.sha256).hexdigest()
    # print(sign.upper())
    return sign.upper()


def headers():
    header = {'request-id': '1', 'request-agent': '1',
              'device-id': '867779032708951', 'os-version': '1', 'phone-model': 'ALP-AL00',
              'sdk-version': '10', 'market': 'baidu', 'app-version': '1.0.0', 'app-version-code': '1.0.0', 'app-name': '1',
              'app-clone-name': '001', 'biz-code': '', 'app-id': appId, 'timestamp': timestamp, 'sign': hmac_sha256(key, appSecret),
              "Content-Type": "application/x-www-form-urlencoded;charset=utf-8"}
    return header


def form_headers():
    header = {'request-id': '1', 'request-agent': '1',
              'device-id': '867779032708951', 'os-version': '1', 'phone-model': 'ALP-AL00',
              'sdk-version': '10', 'market': 'baidu', 'app-version': '1.0.0', 'app-version-code': '1.0.0', 'app-name': '1',
              'app-clone-name': '001', 'biz-code': '', 'app-id': appId, 'timestamp': timestamp, 'sign': hmac_sha256(key, appSecret),
              "Content-Type": "application/x-www-form-urlencoded;charset=utf-8", "access-token": "22920cf3cad8447f806d4fa97e804aa2",
              "customer-id	": "073f36a3c29a4efcae1edf6ca11e024a"}
    return header


def json_headers():
    header = {'request-id': '1', 'request-agent': '1',
              'device-id': '867779032708951', 'os-version': '1', 'phone-model': 'ALP-AL00',
              'sdk-version': '10', 'market': 'baidu', 'app-version': '1.0.0', 'app-version-code': '1.0.0',
              'app-name': '1',
              'app-clone-name': '001', 'biz-code': '', 'app-id': appId, 'timestamp': timestamp,
              'sign': hmac_sha256(key, appSecret),
              "Content-Type": "application/json	", "access-token": "72e75e55158c4cc49877064d4c2ba100",
              "customer-id	": "073f36a3c29a4efcae1edf6ca11e024a"}
    return header
