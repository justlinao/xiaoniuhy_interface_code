import requests
import json
from Public.get_env_yaml import read_config
env = read_config()


def headers():
    header = {'request-id': '1', 'request-agent': '1',
              'device-id': '867779032708951', 'os-version': '1', 'phone-model': 'ALP-AL00',
              'sdk-version': '10', 'market': 'baidu', 'app-version': '1.0.0', 'app-version-code': '1.0.0',
              'app-name': '1',
              'app-clone-name': '001', 'biz-code': '', 'app-id': appId, 'timestamp': timestamp,
              'sign': hmac_sha256(key, appSecret),
              "Content-Type": "application/json;charset=utf-8", "access-token": "22920cf3cad8447f806d4fa97e804aa2",
              "customer-id	": "ba0b31b775714d7782c0dbd12d3fcb13"}
    return header


def customerPhones():
    for i in range(3):
        user_list = list(range(18119676300, 18119676304))
    return user_list
    # for customerPhone in user_list:
    #     print(customerPhone)
    #     return customerPhone


def great_users(customerPhone):
    url = 'http://%s/gateway/customer/customer/registerLogin' % env
    data = {'registerLoginType': '1', 'customerPhone': customerPhone, 'phoneCode': '9527', 'appName': '1',
            'appCloneName': '001',
            'deviceId': '867779032708951', 'osVersion': '1', 'sdkVersion': '10', 'appVersion': '1.0',
            'ipAddress': '192.168.1.1',
            'source': '1'}
    re = requests.post(headers=headers, url=url, data=json.dumps(data))
    # print(re.status_code, re.text)
    re = json.loads(re.text)
    re = re['data']['customerId']
    print(re)
    return re


def customerid_list():
    customerid_list = []  # 创建的customerid 列表
    for i in customerPhones():
        customerid_list.append(great_users(i))
    return customerid_list

# 把customeid 传到请求头中，

def follow():
    url = 'http://%s/gateway/customer/room/follow/saveorcancle' % env
    data = {'followCustomerId': 'a9baf99e9894420a88d482490d9c1946',
            'type': '1'}
    re = requests.post(headers=headers, url=url, data=json.dumps(data))









