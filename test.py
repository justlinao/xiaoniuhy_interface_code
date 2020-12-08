# -*- coding: UTF-8 -*-
# def count_down(n):
#     while n >= 0:
#         newn = yield n
#         print('newn', newn)
#         if newn:
#             print('if')
#             n = newn
#             print('n =', n)
#         else:
#             n -= 1
#
#
# cd = count_down(5)
# for i in cd:
#     print(i, ',')
#     if i == 5:
#         cd.send(3)


def test():
    list = []
    with open(r'C:\Users\linao\Desktop\111.txt', 'r+', encoding='utf-8') as f:
        file = f.read().split()
        for j in file:
            print(j)
            list.append(j)
    print(list)  # 读取文件保存到列表
    f.close()
    new_list = []
    for i in list:  # 查找两个列表不同的元素
        if i not in new_list:
            yield i  # 相同的添加到新列表
        else:
            print(i)  # 不同的打印出来


def test1(fun):
    with open(r'C:\Users\linao\Desktop\111.txt', "w", encoding="utf-8") as f:
        for i in fun:
            print(i)
            f.write(i)


test1(test())





# list = [5, 3, 4, 5, 21, 78]
# count = len(list)
# for i in range(count-1):
#     for j in range(0, count-i-1):
#         if list[j+1] > list[j]:
#             list[j], list[j+1] = list[j+1], list[j]
# print(list)
# for i in range(1, 10):
#     # print("*")
#     for j in range(1, i+1):
#         print("%s*%s=%s" % (i, j, i*j), end='\t')
#     print(' ')


i = "test.gz"
a = i.split(".")[-1]
print(a)


def fun(x):
    return x**2


list = [1, 2, 3, 4, 5]
lis = map(fun, list)
y = [i for i in lis if i > 10]
print(y)