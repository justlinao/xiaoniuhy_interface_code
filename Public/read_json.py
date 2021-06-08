# -*- coding: UTF-8 -*-
import json
import os

path = os.path.dirname(__file__)

with open(path+"/demo.json", encoding="utf-8") as f:
    data = json.load(f)
    print(data)

# list = [1, 5, 9, 4]
# for i in range(1, len(list)):  # 循环遍历气泡的次数
#     for j in range(0, len(list)-i):  # 每次气泡对比的次数
#         if list[j] > list[j+1]:
#             list[j], list[j+1] = list[j+1], list[j]
# print(list)


"""
 json.dumps()用于将dict类型的数据转成str
 json.loads()用于将str类型的数据转成dict
 
 json.dump()用于将dict类型的数据转成str，并写入到json文件中
 json.dump(dict, open(json文件, "w"))
 
 json.load()用于从json文件中读取数据，并以字典类型储存
 emb_filename = ('/home/cqh/faceData/emb_json.json')     
 jsObj = json.load(open(emb_filename))       
 print(jsObj)  
 print(type(jsObj))   
 for key in jsObj.keys():  
    print('key: %s   value: %s' % (key,jsObj.get(key)))
"""
