# -*- coding: UTF-8 -*-
import requests
from Public.req_header import headers

headers = headers()
import json


def forbidden_save():
    url = 'http://qx-fat.qianshi188.com/gateway/room/forbidden/save'
    data = {"roleType": 3, "roomId": "bc7266fac7bf4e35ae058519c235a4fb",
            "blackCustomerId": "bc7266fac7bf4e35ae058519c235a4fb",
            "operationBehavior": 13, "forbiddenTimeType": 98, "appUid": "822222797", "nickName": "我是测试2号",
            "operationFunction": 1, "roomCustomerId": "e3f5e71418054e759a1c36d94cb18f89",
            "liveDetailId": "0694e36718ca44aa9c9d9fd3aa22911a",
            "operationDesc": "警告一次", "liveNickName": "我是测试2号",
            }

    re = requests.post(url=url, headers=headers, data=json.dumps(data))
    text = "举报接口执行结果："
    text = text + str(re.status_code)
    return re.status_code


forbidden_save()


