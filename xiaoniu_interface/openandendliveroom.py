# -*- coding: UTF-8 -*-
from Public.db import *
import time
import hmac
import hashlib
import requests
import json
timestamp = str(int(time.time()))
appId = '1149954699146534912'
key = appId + str(timestamp)
appSecret = '16a9cc89a54511e993fc506b4bbe1bc4'


def hmac_sha256(key, appSecret):
    """
    hmacsha256加密
    return:加密结果转成16进制字符串形式
    """
    message = appSecret.encode('utf-8')
    sign = hmac.new(key.encode('utf-8'), message, digestmod=hashlib.sha256).hexdigest()
    # print(sign.upper())
    return sign.upper()


class test_db(DB):
    # 跨库两表联查customerId
    def test_query(self):
        re = DB.query_db(self,
                         "SELECT c.customer_id FROM qx_live_customer_test.customer c LEFT JOIN qx_live_room_test.live_room r ON c.customer_id = r.customer_id WHERE c.identity = 2 AND c.customer_phone LIKE '%15488880%' AND r.room_ban_status = 1 AND r.live_status = 0 LIMIT 0, 1000")
        print(re)
        return re

    # 跨库两表联查roomId
    def new_anchor_room_Id(self):
        DB.query_db(self,
                    "SELECT r.room_id FROM qx_live_customer_test.customer c LEFT JOIN qx_live_room_test.live_room r ON c.customer_id = r.customer_id WHERE c.identity = 2 AND c.customer_phone LIKE '%15488880%' AND r.room_ban_status = 1")

    #   查询自己造的正在开播中状态的所有直播数据
    def select_Mydata_customerId(self):
        re = DB.query_db(self, "SELECT customer_id FROM 	qx_live_room_test.live_room WHERE 	`cover_url` = 'http://pic.netbian.com/uploads/allimg/180524/210359-152716703985f1.jpg' AND `live_status` = '1' AND room_ban_status = 1 LIMIT 0,  1000")
        return re

    def select_Mydata_roomId(self):
        re = DB.query_db(self, "SELECT room_id FROM 	qx_live_room_test.live_room WHERE 	`cover_url` = 'http://pic.netbian.com/uploads/allimg/180524/210359-152716703985f1.jpg' AND `live_status` = '1' AND room_ban_status = 1 LIMIT 0,  1000")
        return re

    def select_Mydata_liveDetailId(self):
        re = DB.query_db(self, "SELECT live_detail_id FROM 	qx_live_room_test.live_room WHERE 	`cover_url` = 'http://pic.netbian.com/uploads/allimg/180524/210359-152716703985f1.jpg' AND `live_status` = '1' LIMIT 0,  1000")
        return re


def start_live():  # 开启直播
    # customerId_list = anchor_customer_Id()
    i = 1
    #   【主播查询自己直播间信息】
    query_roomId_url = "http://qx-fat.qianshi188.com/gateway/room/liveroom/queryownliveroom"

    for read_list in test_db().test_query():
        header = {'request-id': '1', 'request-agent': '1',
                  'device-id': '867779032708951', 'os-version': '1', 'phone-model': 'ALP-AL00',
                  'sdk-version': '10', 'market': 'baidu', 'app-version': '1.0.0', 'app-version-code': '1.0.0',
                  'app-name': '1',
                  'app-clone-name': '001', 'biz-code': '', 'app-id': appId, 'timestamp': timestamp,
                  'sign': hmac_sha256(key, appSecret),
                  "Content-Type": "application/json;charset=utf-8",
                  "access-token": None,
                  "customer-id	": read_list}
        data = {}
        re = requests.post(headers=header, url=query_roomId_url, data=json.dumps(data))
        print(re.text)
        re = json.loads(re.text)
        roomId = re["data"]["roomId"]

        #  开播操作
        url_start_live = "http://qx-fat.qianshi188.com/gateway/room/liveroom/startlive"
        start_live_data = {
            "roomId": roomId,
            "roomTitle": "直播标题：" + str(i),
            "coverUrl": "http://pic.netbian.com/uploads/allimg/180524/210359-152716703985f1.jpg"
        }
        res_start_live = requests.post(url=url_start_live, data=json.dumps(start_live_data))

        i = i + 1

#   查询并关播操作
def select_room_list():
    result_liveDetailId = []
    result_roomId = []
    result_customer_id = []

    header = {'request-id': '1', 'request-agent': '1',
              'device-id': '867779032708951', 'os-version': '1', 'phone-model': 'ALP-AL00',
              'sdk-version': '10', 'market': 'baidu', 'app-version': '1.0.0', 'app-version-code': '1.0.0',
              'app-name': '1',
              'app-clone-name': '001', 'biz-code': '', 'app-id': appId, 'timestamp': timestamp,
              'sign': hmac_sha256(key, appSecret),
              "Content-Type": "application/json;charset=utf-8",
              "access-token": None,
                }

    #   查询当前所有开播数据

    #   测试环境
    select_room_list_url = "http://qx-fat.qianshi188.com/gateway/room/liveroom/queryliveroomlist"

    #   开发环境
    # select_room_list_url = "http://qx-dev.adtopmob.com/gateway/room/liveroom/queryliveroomlist"
    select_room_list_data = {
                                "page": "1",
                                "size": "1000",
                                "liveTypeId": None
    }
    res_select = requests.post(url=select_room_list_url, headers=header, data=json.dumps(select_room_list_data))
    res_select = json.loads(res_select.text)
    live_details_res = res_select["data"]["list"]

    #   根据接口返回，取值
    for read_list in live_details_res:
        result_customer_id.append(read_list["customerId"])
        result_roomId.append(read_list["roomId"])
        result_liveDetailId.append(read_list["liveDetailId"])

    print(type(result_customer_id), len(result_customer_id), result_customer_id)
    print(type(result_roomId), len(result_roomId), result_roomId)
    print(type(result_liveDetailId), len(result_liveDetailId), result_liveDetailId)

    #   关播操作
    #   执行关播操作
    for i in range(len(result_roomId)):

        #   开发环境
        # endlive_url = "http://qx-dev.adtopmob.com/gateway/room/liveroom/endlive"

        #   测试环境
        endlive_url = "http://qx-fat.qianshi188.com/gateway/room/liveroom/endlive"
        header = {'request-id': '1', 'request-agent': '1',
                  'device-id': '867779032708951', 'os-version': '1', 'phone-model': 'ALP-AL00',
                  'sdk-version': '10', 'market': 'baidu', 'app-version': '1.0.0', 'app-version-code': '1.0.0',
                  'app-name': '1',
                  'app-clone-name': '001', 'biz-code': '', 'app-id': appId, 'timestamp': timestamp,
                  'sign': hmac_sha256(key, appSecret),
                  "Content-Type": "application/json;charset=utf-8",
                  "access-token": None,
                  "customer-id": result_customer_id[i],
                  }

        endlive_data = {
                            "roomId": result_roomId[i],
                            "liveDetailId": result_liveDetailId[i]
                }

        res_endlive = requests.post(url=endlive_url, headers=header, data=json.dumps(endlive_data))
        print(res_endlive.text)

    #   查询当前所有开播数据总数

#   关闭我自己创建的所有开播状态的直播间
def endlive():
    result_customer_id = test_db().select_Mydata_customerId()
    result_roomId = test_db().select_Mydata_roomId()
    result_liveDetailId = test_db().select_Mydata_liveDetailId()
    print(type(result_customer_id), len(result_customer_id), result_customer_id)
    print(type(result_roomId), len(result_roomId), result_roomId)
    print(type(result_liveDetailId), len(result_liveDetailId), result_liveDetailId)

    for i in range(len(result_roomId)):
        endlive_url = "http://qx-fat.qianshi188.com/gateway/room/liveroom/endlive"
        header = {'request-id': '1', 'request-agent': '1',
                  'device-id': '867779032708951', 'os-version': '1', 'phone-model': 'ALP-AL00',
                  'sdk-version': '10', 'market': 'baidu', 'app-version': '1.0.0', 'app-version-code': '1.0.0',
                  'app-name': '1',
                  'app-clone-name': '001', 'biz-code': '', 'app-id': appId, 'timestamp': timestamp,
                  'sign': hmac_sha256(key, appSecret),
                  "Content-Type": "application/json;charset=utf-8",
                  "access-token": None,
                  "customer-id": result_customer_id[i],
                  }

        endlive_data = {
                            "roomId": result_roomId[i],
                            "liveDetailId": result_liveDetailId[i]
                }

        requests.post(url=endlive_url, headers=header, data=json.dumps(endlive_data))

# start_live()  # 开播
# select_room_list()  # 关闭所有直播间

