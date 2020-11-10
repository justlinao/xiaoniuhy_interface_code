# -*- coding: UTF-8 -*-
"""for循环遍历列表，将列表中小元组的key和value取出，作为字典的key：value"""
# list = [('a', 'b'), ('c', 'd')]
# dic = {key: value for key, value in list}
# print(dic)

"""通过字典推导式+zip 组合两个列表成字典"""
# t_list = [1, 2, 3, 4]
# list1 = ['a', 'b', 'c', 'd']
# z = zip(t_list, list1)
# dic1 = {t_list: list1 for t_list, list1 in z}
# print(dic1)
#
#
# for key, value in dic1.items():
#     print(key, value)


list_1 = [1, 2, 3, 4]
lits_2 = ['a', 'b', 'c', 'd']
dic = {}
for i in range(len(list_1)):
    print(list_1[i])
    dic[list_1[i]] = lits_2[i]

print(dic)
