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
    new_str = ''
    with open(r'C:\Users\linao\Desktop\111.txt', 'r+', encoding='utf-8') as f:
        file = f.read().split()
        for i in file:
            list.append(i)
    print(list)  # 读取文件保存到列表
    new_list = []
    for i in list:  # 查找两个列表不同的元素
        if i not in new_list:
            new_list.append(i)  # 相同的添加到新列表
            new_str = new_str + i + "\n"
            print(new_str)
        else:
            print(i)  # 不同的打印出来
    print(new_list)
    print(new_str)
    f.close()
    with open(r'C:\Users\linao\Desktop\111.txt', "w", encoding="utf-8") as f:
        f.write(new_str)
    f.close()
    return new_list


# def test1(list):
#     with open(r'C:\Users\linao\Desktop\111.txt', 'w', encoding='utf-8') as f:
#         for i in list:
#             f.write(i)
#             f.write("\r\n")
#
#     f.close()
#

test()

