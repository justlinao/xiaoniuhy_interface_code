# -*- coding: UTF-8 -*-
def test():
    """
    去除相同的渠道
    :return: 返回去重后的列表
    """
    list = []
    with open(r'C:\Users\linao\Desktop\渠道.txt', 'r+', encoding='utf-8') as f:
        file = f.read().split()
        for i in file:
            list.append(i)
    # print(list)  # 读取文件保存到列表
    new_list = []
    for i in list:  # 查找两个列表不同的元素
        if i not in new_list:
            new_list.append(i)  # 相同的添加到新列表
        else:
            print(i)  # 不同的打印出来
    print(new_list)
    count = 0
    with open(r'C:\Users\linao\Desktop\渠道.txt', 'w', encoding='utf-8') as f:
        for i in new_list:
            # print(i)
            count += 1
            f.write(i + '\n')
            # print("已写入%s个渠道号" % count)
        print("去重后共写入---%s---条，写入完毕" % count)
    return new_list


def test_1(list):
    """
    拆分不同的渠道写入不同的文件
    :param list: 接收渠道列表
    :return: 返回4个渠道txt文件
    """
    list_365 = []
    list_xigua =[]
    list_xiangyun = []
    list_zaowan = []
    tianqi_365 = 0
    tianqi_zaowan = 0
    tianqi_xigua = 0
    tianqi_xiangyun = 0
    for i in list:
        if i.startswith('365wt'):
            list_365.append(i)

        elif i.startswith('zwwt'):
            list_zaowan.append(i)

        elif i.startswith('xgwt'):
            list_xigua.append(i)

        else:
            i.startswith('xywt')
            list_xiangyun.append(i)

    with open(r'C:\Users\linao\Desktop\365.txt', 'w+', encoding='utf-8') as f:
        for k in list_365:
            f.write(k + '\n')
            tianqi_365 += 1
    with open(r'C:\Users\linao\Desktop\zaowan.txt', 'w+', encoding='utf-8') as f:
        for l in list_zaowan:
            f.write(l + '\n')
            tianqi_zaowan += 1
    with open(r'C:\Users\linao\Desktop\xigua.txt', 'w+', encoding='utf-8') as f:
        for m in list_xigua:
            f.write(m + '\n')
            tianqi_xigua += 1
    with open(r'C:\Users\linao\Desktop\xiangyun.txt', 'w+', encoding='utf-8') as f:
        for n in list_xiangyun:
            f.write(n + '\n')
            tianqi_xiangyun += 1
    print("写入365天气%s条" % tianqi_365)
    print("写入早晚天气%s条" % tianqi_zaowan)
    print("写入西瓜天气%s条" % tianqi_xigua)
    print("写入祥云天气%s条" % tianqi_xiangyun)


test_1(test())





