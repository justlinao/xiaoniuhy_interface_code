# -*- coding: UTF-8 -*-
import requests
from Public.req_header import form_headers

headers = form_headers()
import json


def query_backpage_num():
    url = "http://qx-fat.qianshi188.com/gateway/gift/gift/knapsack/unread"
    re = requests.post(url=url, headers=headers, data=None)
    print(re.text)


query_backpage_num()
