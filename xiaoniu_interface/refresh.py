# -*- coding: UTF-8 -*-
"""
排行榜定时任务
"""
import requests
import json
from Public.req_header import login_headers
import time
headers = login_headers()
dev = 'qx-dev.adtopmob.com'
test = 'qx-fat.qianshi188.com'


def refresh():
    url = 'http://qx-fat.qianshi188.com/gateway/gift/rank/job'
    # data = {'appName': '1', 'customerId': 'a852005cdc0b4c9ebfb36b2470bbaced',
    #         'coverUrl': 'https://dss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=317739672,1369082404&fm=26&gp=0.jpg'}
    re = requests.post(headers=headers, url=url, data=None)
    print(re.status_code, re.text, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


while True:
    refresh()
    time.sleep(10)
    print('------------***********------------------------------------------------------------------------------------')
