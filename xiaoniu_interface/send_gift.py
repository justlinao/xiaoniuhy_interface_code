import requests
import json
from Public.req_header import json_headers
from Public.get_env_yaml import read_config
from xiaoniu_interface.start_live import startlive
headers = json_headers()


def sendgift():
    url = "http://qx-fat.qianshi188.com/gateway/gift/gift/send"
    data = {""}
    re = requests.post(url=url, headers=headers, data=None)

