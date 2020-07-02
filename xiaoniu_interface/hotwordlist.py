import requests
from Public.req_header import headers
headers = headers()


def hotword():
    url = 'http://qx-fat.qianshi188.com/gateway/room/livehotword/querylivehotwordlist'
    data = {''}
    re = requests.post(headers=headers, url=url, data=data)
    print(re.status_code, re.text)


hotword()
