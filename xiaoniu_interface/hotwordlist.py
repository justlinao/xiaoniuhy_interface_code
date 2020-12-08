# -*- coding: UTF-8 -*-
import requests
from Public.req_header import headers
headers = headers()


def hotword():
    url = 'http://qx-fat.qianshi188.com/gateway/room/livehotword/querylivehotwordlist'
    data = {''}
    re = requests.post(headers=headers, url=url, data=data)
    text = "热词接口执行结果："
    text = text + str(re.status_code)
    return text


hotword()
