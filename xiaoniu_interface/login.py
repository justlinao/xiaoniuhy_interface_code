import requests
import json
from Public.req_header import headers
from Public.get_env_yaml import read_config
headers = headers()
env = read_config()
# print(env)


def login(customerPhone, phoneCode):
    # url = 'http://%s/gateway/customer/customer/registerLogin' % env
    url = 'http://127.0.0.1:5000/login'
    data = {'registerLoginType': '1', 'customerPhone': customerPhone, 'phoneCode': phoneCode, 'appName': '1',
            'appCloneName': '001',
            'deviceId': '867779032708951', 'osVersion': '1', 'sdkVersion': '10', 'appVersion': '1.0',
            'ipAddress': '192.168.1.1',
            'source': '1'}
    re = requests.post(headers=headers, url=url, data=json.dumps(data))
    # print(re.status_code, re.text)
    # re = json.loads(re.text)
    return re.status_code
    # customerToken = re['data']['customerToken']
    # print(customerToken)
    # return customerToken


if __name__ == '__main__':
    login('18111111111', '9527')
