# -*- coding: UTF-8 -*-
import copy
a = [1, 2, 3]
# print(id(a))
# b = a.copy()
# print(b)
# print(id(b))
a.append(4)
# print(b)


c = copy.deepcopy(a)
print("原始a的地址%s  " % (id(a)))
print("原始c的地址%s  " % (id(c)))
print("原始的a=%s " % a)
print("原始的c=%s " % c)
a.append(5)
print("修改后的a=%s " % a)
print("查看c 是否变化 c=%s " % c)

