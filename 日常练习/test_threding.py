# -*- coding: UTF-8 -*-

import threading
from xiaoniu_interface.my_test import my_login
import time
import requests
import json


def my_print():
    url = "http://weathergameserver.mloveli.com/user/exchange_rmb"
    data = {
        "data": {
            "cash_id": 1,
            "client_ip": "",
            "imei": ""
        },
        "open_id": "oBk7W6Y6iKxy5a2EUnLvm7_6s4Kk"
    }
    re = requests.post(url=url, data=json.dumps(data))
    print(re.text)


if __name__ == '__main__':
    start = time.time()
    for i in range(100):
        t = threading.Thread(target=my_print)
        time.sleep(1)
        t.start()

    end = time.time()
    print(end-start)

