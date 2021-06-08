# -*- coding: UTF-8 -*-
"""
获取接口请求耗时，装饰器
"""
import time


def res_time(fuc):
    def inner(*args, **kwargs):
        start_time = int(time.time() * 1000)
        fuc(*args, **kwargs)
        end_time = int(time.time() * 1000)
        consume_time = end_time - start_time
        # print(consume_time)
        return [consume_time, fuc(*args, **kwargs)]  # fuc(*args, **kwargs)被装饰函数的return返回值
    return inner







