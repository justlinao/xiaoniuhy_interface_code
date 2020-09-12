# -*- coding: UTF-8 -*-
def test():
    list = []
    with open(r'C:\Users\linao\Desktop\111.txt', 'r+', encoding='utf-8') as f:
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
    with open(r'C:\Users\linao\Desktop\111.txt', 'w', encoding='utf-8') as f:
        for i in new_list:
            # print(i)
            count += 1
            f.write(i + '\n')
            print("已写入%s个渠道号" % count)
        print("共写入---%s---条，写入完毕" % count)


test()





