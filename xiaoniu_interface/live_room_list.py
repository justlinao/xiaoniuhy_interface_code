import requests
import json
from Public.req_header import login_headers
headers = login_headers()


def liveroomlist():
    url = 'http://qx-fat.qianshi188.com/gateway/room/liveroom/queryliveroomlist'
    data = {'page': '1', 'size': '10'}
    re = requests.post(headers=headers, url=url, data=json.dumps(data))
    print(re.status_code, re.text)


liveroomlist()
