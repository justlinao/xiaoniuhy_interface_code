# -*- coding: UTF-8 -*-
import redis
ip = '172.16.11.68'
password = 'fzcfQwuMH2q'

r = redis.Redis(host=ip, password=password, port=6379, db=1)

res = r.get('lrx2')
print(res)  # ：b'\xe5\x97\xafohyeah234324'
# 结果是二进制类型的，需要将二进制类型的转成字符串类型 res.decode()
# .decode()是二进制类型转成字符串
print(res.decode())  # 结果为：嗯ohyeah234324
