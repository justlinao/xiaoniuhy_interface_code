#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/5/28 11:47
# @Author : fanggang
# @File : xiaoniu_init_account.py
# @Software: PyCharm
# -------------------------------
import sqlite3
import time
import hmac
import random
import hashlib
from public.Tool import Tool
from public.Tool import get_timestamp1
from public.MySqlUtil import MySqlUtil
from public.HttpRequests import HttpRequests
import unittest
from HTMLReport import logger
from public.KelaEnum import KeLaEnum
from public.Tool import Tool
import requests


timestamp = str(int(time.time()))
#appId = '1149954699146534912'



appId = "1149960309183299584"
deviceId = "A17EFC0B198941CBA693915B5A0B4472"
str_a = appId + get_timestamp1() + deviceId
appSecret = "1acdf792a54511e993fc506b4bbe1bc4"


def sign_alg(str_a,security):
    r_str_a = bytes((str_a).encode('utf-8'))
    r_security = bytes((security).encode('utf-8'))

    sign = (hmac.new(r_security, r_str_a, digestmod=hashlib.sha256)).hexdigest().upper()
    return sign

def hmac_sha256(key, appSecret):
    """
    hmacsha256加密
    return:加密结果转成16进制字符串形式
    """
    message = appSecret.encode('utf-8')
    sign = hmac.new(key.encode('utf-8'), message, digestmod=hashlib.sha256).hexdigest()
    # print(sign.upper())
    return sign.upper()

# 内置函数，性能最优
def user_data():
    user_list = list(range(15488881050, 15488881051))
    return user_list

# 查询所有【可以开播】 且 开播状态为【未开播】 且 【未被封禁】的roomId
def is_anchor():
    sql_str = "SELECT room_id FROM qx_live_room_test.live_room WHERE live_status = 0 and room_ban_status =1"
    result_anchor = MySqlUtil().mysql_get_result_list(sql_str)
    return result_anchor

def anchor_customer_Id():
    #sql_str = "SELECT customer_Id FROM qx_live_room_test.live_room WHERE room_ban_status = 1"
    sql_str = "SELECT customer_Id FROM qx_live_room_test.live_room WHERE live_status = 0 and room_ban_status = 1"
    result_anchor = MySqlUtil().mysql_get_result_list(sql_str)
    return result_anchor

#   跨库两表联查
def new_anchor_customer_Id():
    sql_str = "SELECT c.customer_id FROM qx_live_customer_test.customer c LEFT JOIN qx_live_room_test.live_room r ON c.customer_id = r.customer_id WHERE c.identity = 2 AND c.customer_phone LIKE '%15488880%' AND r.room_ban_status = 1 AND r.live_status = 0 LIMIT 0, 1000"
    #sql_str = "SELECT customer_Id FROM `customer` WHERE `customer_phone` LIKE '%15488880%' AND `identity` LIKE '%2%' LIMIT 0, 150"
    result_anchor = MySqlUtil().mysql_get_result_list(sql_str)
    return result_anchor

#   跨库两表联查roomId
def new_anchor_room_Id():
    sql_str = "SELECT r.room_id FROM qx_live_customer_test.customer c LEFT JOIN qx_live_room_test.live_room r ON c.customer_id = r.customer_id WHERE c.identity = 2 AND c.customer_phone LIKE '%15488880%' AND r.room_ban_status = 1"
    result_room_Id = MySqlUtil().mysql_get_result_list(sql_str)
    return result_room_Id

#   查询自己造的正在开播中状态的所有直播数据
def select_Mydata_customerId():
    sql_str_customerId = "SELECT customer_id FROM 	qx_live_room_test.live_room WHERE 	`cover_url` = 'http://pic.netbian.com/uploads/allimg/180524/210359-152716703985f1.jpg' AND `live_status` = '1' AND room_ban_status = 1 LIMIT 0,  1000"
    result_customerId = MySqlUtil().mysql_get_result_list(sql_str_customerId)
    return result_customerId

def select_Mydata_roomId():
    sql_str_roomId = "SELECT room_id FROM 	qx_live_room_test.live_room WHERE 	`cover_url` = 'http://pic.netbian.com/uploads/allimg/180524/210359-152716703985f1.jpg' AND `live_status` = '1' AND room_ban_status = 1 LIMIT 0,  1000"
    result_roomId = MySqlUtil().mysql_get_result_list(sql_str_roomId)
    return result_roomId

def select_Mydata_liveDetailId():
    sql_str_liveDetailId = "SELECT live_detail_id FROM 	qx_live_room_test.live_room WHERE 	`cover_url` = 'http://pic.netbian.com/uploads/allimg/180524/210359-152716703985f1.jpg' AND `live_status` = '1' LIMIT 0,  1000"
    result_liveDetailId = MySqlUtil().mysql_get_result_list(sql_str_liveDetailId)
    return result_liveDetailId

#   将准备开播的主播数据，添加到其他分类标签中
def add_anchor_game():
    room_Id = new_anchor_room_Id()
    i = 100
    for read_list in room_Id:
        sql_str = "INSERT INTO `qx_live_room_test`.`live_room_type` (`room_type_id`, `app_name`, `room_id`, `live_type_id`, `create_time`) VALUES ('" + str(i) + "', '1', '" + read_list + "', '游戏', '2020-06-11 22:46:11')"
        print(sql_str)
        result = MySqlUtil().mysql_execute(sql_str)
        i = i + 1

def send_code():

    user_list = user_data()

    customerId_list = []

    url_send_code = "http://qx-fat.qianshi188.com/gateway/customer/customer/sendPhoneCode"

    url_register_login = "http://qx-fat.qianshi188.com/gateway/customer/customer/registerLogin"

    for i in user_list:

        send_code_parm = {
            "customerPhone":str(i),
            "sendType":"1"
        }

        register_Login_parm = {
            "registerLoginType": "1",
            "customerPhone": str(i),
            "phoneCode": "9527",
            "appName": "1",
            "appCloneName": "001",
            "deviceId": "f3c481531b7c0cc9",
            "osVersion": "1",
            "sdkVersion": "29",
            "appVersion": "1.0.0",
            "ipAddress": "172.16.7.83",
            "source": "1",
            "market": "tencent"
        }
        header = {
            "request-id": "7B142B65-A3A4-4F63-8C90-50FB9ADB6817-1590994839806",
            "request-agent": "2",
            "device-id": "A17EFC0B198941CBA693915B5A0B4472",
            "os-version": "1",
            "phone-model": "iPhone11,6",
            "sdk-version": "13.4",
            "market": "app_store",
            "app-version": "1.0.0",
            "app-version-code": "100",
            "app-name": "1",
            "app-clone-name": "001",
            "biz-code": "http://qx-dev.adtopmob.com/gateway/customer/anchor/initializeAnchor",
            "app-id": "1149960309183299584",
            "timestamp": get_timestamp1(),
            "sign": sign_alg(str_a, appSecret),
            "customer-id": "",
            "access-token": None,
            "gps-lng": "23.26",
            "gps-lat": "23.26",
            "Content-Type": "application/json;charset=utf-8"
        }
        #   发送验证码
        # res_send_code = HttpRequests().send_r(method='post', u=url_send_code, d=None, j=send_code_parm, h=header)
        # print(res_send_code)
        #   手机号验证码登录，创建一个customerId
        res_register_Login = HttpRequests().send_r(method='post', u=url_register_login,d=None,j=register_Login_parm, h=header).json()

        customerId_list.append(res_register_Login["data"]["customerId"])

    return customerId_list

#   完善用户资料
def update_message():

    customerId_list = send_code()

    # 完善用户资料------url
    url_update_message = "http://qx-fat.qianshi188.com/gateway/customer/customer/editPersonalData"

    # 初始化用户主播身份------url
    url_init_Anchor = "http://qx-fat.qianshi188.com/gateway/customer/anchor/initializeAnchor"

    j = 500
    for i in customerId_list:
        header = {
            "request-id": "7B142B65-A3A4-4F63-8C90-50FB9ADB6817-1590994839806",
            "request-agent": "2",
            "device-id": "A17EFC0B198941CBA693915B5A0B4472",
            "os-version": "1",
            "phone-model": "iPhone11,6",
            "sdk-version": "13.4",
            "market": "app_store",
            "app-version": "1.0.0",
            "app-version-code": "100",
            "app-name": "1",
            "app-clone-name": "001",
            "biz-code": "/customer/customer/editPersonalData",
            "app-id": "1149960309183299584",
            "timestamp": get_timestamp1(),
            "sign": sign_alg(str_a, appSecret),
            "customer-id": str(i),
            "access-token": None,
            "gps-lng": "23.26",
            "gps-lat": "23.26",
            "Content-Type": "application/json;charset=utf-8"
        }

        # 完善用户资料------请求参数
        update_message_parm = {
                                "customerId": str(i),
                                "nickName": "一只大阿giao" + str(j),
                                "signName": str(random.randint(1,500000000)),
                                "customerSex": "1",
                                "birthday": "1999-05-05",
                                "headUrl": "http://pic.netbian.com/uploads/allimg/200604/001849-15912011292fcb.jpg"
        }

        # 初始化主播身份------请求参数
        init_anchor_parm = {
            "appName": 1,
            "customerId": str(i),
            "coverUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590749017466&di=2a741f8e32fddf7ed4c17dba0934cf25&imgtype=0&src=http%3A%2F%2Fc.hiphotos.baidu.com%2Fzhidao%2Fpic%2Fitem%2Ff3d3572c11dfa9ecc052be8060d0f703918fc12d.jpg"
        }

        res_update_message = HttpRequests().send_r(method='post', u=url_update_message,d=None,j=update_message_parm, h=header).json()

        res_init_message = HttpRequests().send_r(method='post', u=url_init_Anchor,d=None,j=init_anchor_parm, h=header).json()

        j = j + 1

#开启直播
def start_live():
    customerId_list = new_anchor_customer_Id()
    #customerId_list = anchor_customer_Id()

    i = 1
    #   【主播查询自己直播间信息】
    select_roomId_url = "http://qx-fat.qianshi188.com/gateway/room/liveroom/queryownliveroom"

    for read_list in customerId_list:
        header = {
            "request-id": "7B142B65-A3A4-4F63-8C90-50FB9ADB6817-1590994839806",
            "request-agent": "2",
            "device-id": "A17EFC0B198941CBA693915B5A0B4472",
            "os-version": "1",
            "phone-model": "iPhone11,6",
            "sdk-version": "13.4",
            "market": "app_store",
            "app-version": "1.0.0",
            "app-version-code": "100",
            "app-name": "1",
            "app-clone-name": "001",
            "biz-code": "/gateway/room/liveroom/queryliveroom",
            "app-id": "1149960309183299584",
            "timestamp": get_timestamp1(),
            "sign": sign_alg(str_a, appSecret),
            "customer-id": read_list,
            "access-token": None,
            "gps-lng": "23.26",
            "gps-lat": "23.26",
            "Content-Type": "application/json;charset=utf-8"
        }

        res_one = HttpRequests().send_r(method='post', u=select_roomId_url,d=None,j=None, h=header).json()

        roomId = res_one["data"]["roomId"]

        #   开播操作
        url_start_live = "http://qx-fat.qianshi188.com/gateway/room/liveroom/startlive"
        start_live_data = {
                            "roomId": roomId,
                            "roomTitle": "直播标题：" + str(i),
                            "coverUrl": "http://pic.netbian.com/uploads/allimg/180524/210359-152716703985f1.jpg"
        }
        res_start_live = HttpRequests().send_r(method='post', u=url_start_live,d=None,j=start_live_data, h=header).json()

        i = i + 1

#   查询并关播操作
def select_room_list():

    result_liveDetailId= []
    result_roomId = []
    result_customer_id = []

    header = {
        "request-id": "7B142B65-A3A4-4F63-8C90-50FB9ADB6817-1590994839806",
        "request-agent": "2",
        "device-id": "A17EFC0B198941CBA693915B5A0B4472",
        "os-version": "1",
        "phone-model": "iPhone11,6",
        "sdk-version": "13.4",
        "market": "app_store",
        "app-version": "1.0.0",
        "app-version-code": "100",
        "app-name": "1",
        "app-clone-name": "001",
        "biz-code": "/room/liveroom/queryliveroomlist",
        "app-id": "1149960309183299584",
        "timestamp": get_timestamp1(),
        "sign": sign_alg(str_a, appSecret),
        "customer-id": "15425c51b4784df19535c7e017485a3e",
        "access-token": None,
        "gps-lng": "23.26",
        "gps-lat": "23.26",
        "Content-Type": "application/json;charset=utf-8"
    }

    #   查询当前所有开播数据

    #   测试环境
    select_room_list_url = "http://qx-fat.qianshi188.com/gateway/room/liveroom/queryliveroomlist"

    #   开发环境
    #select_room_list_url = "http://qx-dev.adtopmob.com/gateway/room/liveroom/queryliveroomlist"
    select_room_list_data = {
                                "page":"1",
                                "size":"1000",
                                "liveTypeId":None
    }
    res_select = HttpRequests().send_r(method='post', u=select_room_list_url,d=None,j=select_room_list_data, h=header).json()

    live_details_res = res_select["data"]["list"]

    #   根据接口返回，取值
    for read_list in live_details_res:
        result_customer_id.append(read_list["customerId"])
        result_roomId.append(read_list["roomId"])
        result_liveDetailId.append(read_list["liveDetailId"])

    print(type(result_customer_id), len(result_customer_id), result_customer_id)
    print(type(result_roomId),len(result_roomId),result_roomId)
    print(type(result_liveDetailId),len(result_liveDetailId),result_liveDetailId)


    #   关播操作
    #   执行关播操作
    for i in range(len(result_roomId)):

        #   开发环境
        #endlive_url = "http://qx-dev.adtopmob.com/gateway/room/liveroom/endlive"

        #   测试环境
        endlive_url = "http://qx-fat.qianshi188.com/gateway/room/liveroom/endlive"
        header = {
            "request-id": "7B142B65-A3A4-4F63-8C90-50FB9ADB6817-1590994839806",
            "request-agent": "2",
            "device-id": "A17EFC0B198941CBA693915B5A0B4472",
            "os-version": "1",
            "phone-model": "iPhone11,6",
            "sdk-version": "13.4",
            "market": "app_store",
            "app-version": "1.0.0",
            "app-version-code": "100",
            "app-name": "1",
            "app-clone-name": "001",
            "biz-code": "/room/liveroom/queryliveroomlist",
            "app-id": "1149960309183299584",
            "timestamp": get_timestamp1(),
            "sign": sign_alg(str_a, appSecret),
            "customer-id": result_customer_id[i],
            "access-token": None,
            "gps-lng": "23.26",
            "gps-lat": "23.26",
            "Content-Type": "application/json;charset=utf-8"
        }

        endlive_data = {
                            "roomId":result_roomId[i],
                            "liveDetailId":result_liveDetailId[i]
                }

        res_endlive = HttpRequests().send_r(method='post', u=endlive_url,d=None,j=endlive_data, h=header)
        print(res_endlive)

    #   查询当前所有开播数据总数

#   关闭我自己创建的所有开播状态的直播间
def endlive():
    result_customer_id = select_Mydata_customerId()
    result_roomId = select_Mydata_roomId()
    result_liveDetailId = select_Mydata_liveDetailId()
    print(type(result_customer_id),len(result_customer_id),result_customer_id)
    print(type(result_roomId), len(result_roomId), result_roomId)
    print(type(result_liveDetailId), len(result_liveDetailId), result_liveDetailId)

    for i in range(len(result_roomId)):
        endlive_url = "http://qx-fat.qianshi188.com/gateway/room/liveroom/endlive"
        header = {
            "request-id": "7B142B65-A3A4-4F63-8C90-50FB9ADB6817-1590994839806",
            "request-agent": "2",
            "device-id": "A17EFC0B198941CBA693915B5A0B4472",
            "os-version": "1",
            "phone-model": "iPhone11,6",
            "sdk-version": "13.4",
            "market": "app_store",
            "app-version": "1.0.0",
            "app-version-code": "100",
            "app-name": "1",
            "app-clone-name": "001",
            "biz-code": "/room/liveroom/queryliveroomlist",
            "app-id": "1149960309183299584",
            "timestamp": get_timestamp1(),
            "sign": sign_alg(str_a, appSecret),
            "customer-id": result_customer_id[i],
            "access-token": None,
            "gps-lng": "23.26",
            "gps-lat": "23.26",
            "Content-Type": "application/json;charset=utf-8"
        }

        endlive_data = {
                            "roomId":result_roomId[i],
                            "liveDetailId":result_liveDetailId[i]
                }

        HttpRequests().send_r(method='post', u=endlive_url,d=None,j=endlive_data, h=header)

#   查询当前开播状态的直播间
def select_open_live():
    #   测试环境URL
    select_roomId_url = "http://qx-fat.qianshi188.com/gateway/room/liveroom/queryliveroomlist"

    #   开发环境URL
    #select_roomId_url = "http://qx-dev.adtopmob.com/gateway/room/liveroom/queryliveroomlist"
    select_room_list_data = {
        "page": "1",
        "size": "1000",
        "liveTypeId": None
    }

    header = {
        "request-id": "7B142B65-A3A4-4F63-8C90-50FB9ADB6817-1590994839806",
        "request-agent": "2",
        "device-id": "A17EFC0B198941CBA693915B5A0B4472",
        "os-version": "1",
        "phone-model": "iPhone11,6",
        "sdk-version": "13.4",
        "market": "app_store",
        "app-version": "1.0.0",
        "app-version-code": "100",
        "app-name": "1",
        "app-clone-name": "001",
        "biz-code": "/room/liveroom/queryliveroomlist",
        "app-id": "1149960309183299584",
        "timestamp": get_timestamp1(),
        "sign": sign_alg(str_a, appSecret),
        "customer-id": "15425c51b4784df19535c7e017485a3e",
        "access-token": None,
        "gps-lng": "23.26",
        "gps-lat": "23.26",
        "Content-Type": "application/json;charset=utf-8"
    }

    res_select = HttpRequests().send_r(method='post', u=select_roomId_url, d=None, j=select_room_list_data,
                                       h=header).json()

    openlive_count = res_select["data"]["list"]
    print("-------------------------------------------------------\n","数据类型:------\n",type(openlive_count),"\n数据总数:------\n",len(openlive_count),"\n数据详情:------\n",openlive_count)

#   直播分类列表查询
def select_live_type():
    select_liveType_url = "http://qx-fat.qianshi188.com/gateway/room/livetype/querylivetypelist"
    header = {
        "request-id": "7B142B65-A3A4-4F63-8C90-50FB9ADB6817-1590994839806",
        "request-agent": "2",
        "device-id": "A17EFC0B198941CBA693915B5A0B4472",
        "os-version": "1",
        "phone-model": "iPhone11,6",
        "sdk-version": "13.4",
        "market": "app_store",
        "app-version": "1.0.0",
        "app-version-code": "100",
        "app-name": "1",
        "app-clone-name": "001",
        "biz-code": "/room/liveroom/queryliveroomlist",
        "app-id": "1149960309183299584",
        "timestamp": get_timestamp1(),
        "sign": sign_alg(str_a, appSecret),
        "customer-id": "15425c51b4784df19535c7e017485a3e",
        "access-token": None,
        "gps-lng": "23.26",
        "gps-lat": "23.26",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    HttpRequests().send_r(method='post', u=select_liveType_url, d=None, j=None,
                                       h=header).json()

def init_anchor():
    # 初始化用户主播身份------url
    url_init_Anchor = "http://qx-fat.qianshi188.com/gateway/customer/anchor/initializeAnchor"
    #url_init_Anchor = "http://qx-dev.adtopmob.com/gateway/customer/anchor/initializeAnchor"

    # 初始化主播身份------请求参数
    init_anchor_parm = {
        "appName": 1,
        "customerId": "07633d24be6f473995caf942e09b404d",
        "coverUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590749017466&di=2a741f8e32fddf7ed4c17dba0934cf25&imgtype=0&src=http%3A%2F%2Fc.hiphotos.baidu.com%2Fzhidao%2Fpic%2Fitem%2Ff3d3572c11dfa9ecc052be8060d0f703918fc12d.jpg"
    }

    header = {
        "request-id": "7B142B65-A3A4-4F63-8C90-50FB9ADB6817-1590994839806",
        "request-agent": "2",
        "device-id": "A17EFC0B198941CBA693915B5A0B4472",
        "os-version": "1",
        "phone-model": "iPhone11,6",
        "sdk-version": "13.4",
        "market": "app_store",
        "app-version": "1.0.0",
        "app-version-code": "100",
        "app-name": "1",
        "app-clone-name": "001",
        "biz-code": "http://qx-dev.adtopmob.com/gateway/customer/anchor/initializeAnchor",
        "app-id": "1149960309183299584",
        "timestamp": get_timestamp1(),
        "sign": sign_alg(str_a, appSecret),
        "customer-id": "07633d24be6f473995caf942e09b404d",
        "access-token": None,
        "gps-lng": "23.26",
        "gps-lat": "23.26",
        "Content-Type": "application/json;charset=utf-8"
    }

    res_init_message = HttpRequests().send_r(method='post', u=url_init_Anchor, d=None, j=init_anchor_parm,
                                             h=header).json()
    print(res_init_message["code"])

def select_user_message():
    url_select_message = "http://qx-fat.qianshi188.com/gateway/customer/customer/queryPersonalData"

    data = {"customerId": "6895b2ee2dfc40139e9106f7e779cb7c"}

    header = {
        "request-id": "7B142B65-A3A4-4F63-8C90-50FB9ADB6817-1590994839806",
        "request-agent": "2",
        "device-id": "A17EFC0B198941CBA693915B5A0B4472",
        "os-version": "1",
        "phone-model": "iPhone11,6",
        "sdk-version": "13.4",
        "market": "app_store",
        "app-version": "1.0.0",
        "app-version-code": "100",
        "app-name": "1",
        "app-clone-name": "001",
        "biz-code": "/gateway/room/liveroom/queryliveroom",
        "app-id": "1149960309183299584",
        "timestamp": get_timestamp1(),
        "sign": sign_alg(str_a, appSecret),
        "customer-id": "000ccafb18e842f99819a1f4a6676fd9",
        "access-token": None,
        "gps-lng": "23.26",
        "gps-lat": "23.26",
        "Content-Type": "application/json;charset=utf-8"
    }

    HttpRequests().send_r(method='post', u=url_select_message, d=None, j=data,
                                             h=header).json()

#   批量查询用户资料
def batchQueryUser():
    url_select_message = "http://qx-fat.qianshi188.com/gateway/customer/customer/batchQueryUser"

    data = {"customerIdList": ["6895b2ee2dfc40139e9106f7e779cb7c"]}

    header = {
        "request-id": "7B142B65-A3A4-4F63-8C90-50FB9ADB6817-1590994839806",
        "request-agent": "2",
        "device-id": "A17EFC0B198941CBA693915B5A0B4472",
        "os-version": "1",
        "phone-model": "iPhone11,6",
        "sdk-version": "13.4",
        "market": "app_store",
        "app-version": "1.0.0",
        "app-version-code": "100",
        "app-name": "1",
        "app-clone-name": "001",
        "biz-code": "/gateway/room/liveroom/queryliveroom",
        "app-id": "1149960309183299584",
        "timestamp": get_timestamp1(),
        "sign": sign_alg(str_a, appSecret),
        "customer-id": "000ccafb18e842f99819a1f4a6676fd9",
        "access-token": None,
        "gps-lng": "23.26",
        "gps-lat": "23.26",
        "Content-Type": "application/json;charset=utf-8"
    }

    HttpRequests().send_r(method='post', u=url_select_message, d=None, j=data,
                                                h=header).json()


def rank():
    """
    榜单种类：首页财富榜-TREASURE,
            首页主播榜-ANCHOR,
            直播间粉丝贡献榜-ROOM_TREASURE,
            直播中心贡献榜-ANCHOR_CENTER
    :return:
    """

    url_rank = "http://qx-fat.qianshi188.com/gateway/gift/rank/"

    header = {
        "request-id": "7B142B65-A3A4-4F63-8C90-50FB9ADB6817-1590994839806",
        "request-agent": "2",
        "device-id": "A17EFC0B198941CBA693915B5A0B4472",
        "os-version": "1",
        "phone-model": "iPhone11,6",
        "sdk-version": "13.4",
        "market": "app_store",
        "app-version": "1.0.0",
        "app-version-code": "100",
        "app-name": "1",
        "app-clone-name": "001",
        "biz-code": "/gateway/gift/rank",
        "app-id": "1149960309183299584",
        "timestamp": get_timestamp1(),
        "sign": sign_alg(str_a, appSecret),
        "customer-id": "07055008c7b04faa8e51a5cdb40d68f1",
        "access-token": None,
        "gps-lng": "23.26",
        "gps-lat": "23.26",
        "Content-Type": "application/json;charset=utf-8"
    }

    #   【首页】主播日榜请求参数
    data_day_rank_anchor = {
                    "rankCategory":"ANCHOR",
                    "rankType":"DAY",
                    "anchorId": None,
                    "liveDetailId": None,
    }

    #   【首页】主播周榜请求参数
    data_week_rank_anchor = {
                    "rankCategory":"ANCHOR",
                    "rankType":"WEEK",
                    "anchorId": None,
                    "liveDetailId": None,
    }

    #   【首页】主播月榜请求参数
    data_month_rank_anchor = {
                    "rankCategory":"ANCHOR",
                    "rankType":"MONTH",
                    "anchorId": None,
                    "liveDetailId": None,
    }

    #   【首页】财富日榜请求参数
    data_day_rank_treasure = {
                    "rankCategory":"TREASURE",
                    "rankType":"DAY",
                    "anchorId": None,
                    "liveDetailId": None,
    }

    #   【首页】财富周榜请求参数
    data_week_rank_treasure = {
                    "rankCategory":"TREASURE",
                    "rankType":"WEEK",
                    "anchorId": None,
                    "liveDetailId": None,
    }

    #   【首页】财富月榜请求参数
    data_month_rank_treasure = {
                    "rankCategory":"TREASURE",
                    "rankType":"MONTH",
                    "anchorId": None,
                    "liveDetailId": None,
    }

    #   定时任务
    HttpRequests().send_r(method='post', u="http://qx-fat.qianshi188.com/gateway/gift/rank/job", d=None, j=None,
                          h=header)

    #   主播日榜接口返回数据
    print("主播日榜接口返回数据--------------------------------------------")
    HttpRequests().send_r(method='post', u=url_rank, d=None, j=data_day_rank_anchor,
                          h=header).json()

    #   主播周榜接口返回数据
    print("主播周榜接口返回数据--------------------------------------------")
    HttpRequests().send_r(method='post', u=url_rank, d=None, j=data_week_rank_anchor,
                          h=header).json()

    #   主播月榜接口返回数据
    print("主播月榜接口返回数据--------------------------------------------")
    HttpRequests().send_r(method='post', u=url_rank, d=None, j=data_month_rank_anchor,
                          h=header).json()

    #   财富日榜接口返回数据
    print("财富日榜接口返回数据--------------------------------------------")
    HttpRequests().send_r(method='post', u=url_rank, d=None, j=data_day_rank_treasure,
                          h=header).json()

    #   财富周榜接口返回数据
    print("财富周榜接口返回数据--------------------------------------------")
    HttpRequests().send_r(method='post', u=url_rank, d=None, j=data_week_rank_treasure,
                          h=header).json()

    #   财富月榜接口返回数据
    print("财富月榜接口返回数据--------------------------------------------")
    HttpRequests().send_r(method='post', u=url_rank, d=None, j=data_month_rank_treasure,
                          h=header).json()

#   初始化排行榜数据，查询最新的首页排行榜榜单数据
#rank()

#   查询当前所有开播数据，并执行关播操作
#select_room_list()

#   查询自定义条数的主播身份数据并执行开播操作
#start_live()

#   查询当前所有开播数据总数
#select_open_live()

#   关闭我自己创建的所有开播状态的直播间
#endlive()

#   初始化主播身份
#init_anchor()

#   将主播添加到首页其他分类中去
#add_anchor_game()


































# def register_Login():
#     url_register_login = "http://qx-fat.qianshi188.com/gateway/customer/customer/registerLogin"
#
#     url_save_user_information = "http://qx-fat.qianshi188.com/gateway/customer/customer/editPersonalData"

# url_send_code = "http://qx-fat.qianshi188.com/gateway/customer/customer/sendPhoneCode"
#
# url_register_login = "http://qx-fat.qianshi188.com/gateway/customer/customer/registerLogin"
#
# send_code_parm = {
#     "customerPhone":"15400000022",
#     "sendType":"1"
# }
#
# register_Login_parm = {
#     "registerLoginType": 1,
#     "customerPhone": "15400000022",
#     "phoneCode": "9527",
#     "appName": "1",
#     "appCloneName": "001",
#     "deviceId": "f3c481531b7c0cc9",
#     "osVersion": "1",
#     "sdkVersion": "29",
#     "appVersion": "1.0.0",
#     "ipAddress": "172.16.7.83",
#     "source": "1",
#     "market": "tencent"
# }
# #   发送验证码
# res_send_code = HttpRequests().send_r(method='post', u=url_send_code, d=None, j=send_code_parm, h=header)
#
# #   手机号验证码登录，创建一个customerId
# res_register_Login = HttpRequests().send_r(method='post', u=url_register_login,d=None,j=register_Login_parm, h=header).json()
#
#
# print("-----res_send_code:",res_send_code)
# print("res_register_Login:",res_register_Login)
# print("------------------------------",res_register_Login["data"]["customerId"])





