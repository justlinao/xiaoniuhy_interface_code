import requests
import json
from Public.req_header import login_headers
headers = login_headers()
dev = 'qx-dev.adtopmob.com'
test = 'qx-fat.qianshi188.com'


def init():
    url = 'http://'+dev+'/gateway/customer/anchor/initializeAnchor'
    data = {'appName': '1', 'customerId': '073f36a3c29a4efcae1edf6ca11e024a ',
            'coverUrl': 'https://dss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=317739672,1369082404&fm=26&gp=0.jpg'}
    re = requests.post(headers=headers, url=url, data=json.dumps(data))
    print(re.status_code, re.text)


init()
