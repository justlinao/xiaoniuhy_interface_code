import os
import sys
import shutil
import requests
import time
from pandas import DataFrame, Series


# 设置安卓渠道版本所在目录,ApkTool可不设
version_catalogue = r"/Users/naoli/Desktop/60174-60921"
ApkTool = r"/Users/naoli/Desktop/apktool.jar"
now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

# apktool.jar地址
apktool_download_url = 'https://bitbucket.org/iBotPeaches/apktool/downloads/apktool_2.1.0.jar'


try:
    if os.path.isdir(version_catalogue):
        vapk = [cv for cv in os.listdir(version_catalogue) if os.path.splitext(cv)[1] == '.apk']
        # print(vapk)
        if len(vapk) != 0:
            print(" -> Total: \033[1;37;42m {0} \33[0m Apk. ".format(len(vapk)))
        else:
            print(" -> No has ApkFile.")
            raise NameError
except (NameError, OSError, IOError):
    print(" -> Error: Please check File PATH.")
    sys.exit()
else:
    os.chdir(version_catalogue)

# 拷贝或下载apktool.jar反编译工具
if os.path.exists(os.path.join(version_catalogue, 'apktool.jar')):
    print(" ->{0} Has found a decompiler apktool.jar.\n".format(version_catalogue))
elif os.path.isfile(ApkTool):
    shutil.copy(ApkTool, version_catalogue)
else:
    with open('apktool.jar', 'wb') as atool:
        print(" -> The Computer is not exists apktools.jar,Will begining Download Apktools.jar......")
        atool.write(requests.get(apktool_download_url).content)

start_time = time.time()


# 反编译android apk
def decompiler(vdir):
    """

    :param vdir: 存放apk的文件夹
    :return: apk文件，reverse_apk_folder反编译后文件
    """
    vapk = [cv for cv in os.listdir(vdir) if os.path.splitext(cv)[1] == '.apk']
    print(" -> The Path has found {0} channel version,is in decomopiling,Please wait.....\n".format(len(vapk)))
    for idx, apk in enumerate(vapk):
        channeldir, extension = os.path.splitext(apk)
        if os.path.isdir(channeldir):
            pass
        else:
            print(" -> The \033[1;37;44m {0} \33[0m Apk is processing : {1}".format(idx, apk))
            os.popen('java -jar apktool.jar d -s {0}'.format(apk))
    time.sleep(10)  # 等待编译完成
    reverse_apk_folder = [opf for opf in os.listdir(vdir) if os.path.isdir(opf)]
    print("-------------------------------------------------------------------")
    print(" -> {0} Finish Apk decompiling.".format(now))
    print(" -> Total: \033[1;32;44m {0} \33[0m Apk Floder. ".format(len(reverse_apk_folder)))
    return vapk, reverse_apk_folder


# 处理AndroidManifest.xml文件
def handling(filename, text):
    """

    :param filename: AndroidManifest.xml文件
    :param text: 需求的字段/channel
    :return: channel
    """
    textual_value = ""
    with open(filename, 'r+') as m:
        line = [line.strip() for line in m.readlines() if text in line]
        # print(line)
        for n in line:
            # print(n)
            value = n.split('=')[2]
            # print(value)
            # 使用strip过滤"/>//--等特殊字符
            textual_value = value.strip('"/>// --')
    return textual_value


# 遍历反编译后的apk文件夹，通过AndroidManifest.xml文件获取渠道号
def get_apk_umeng_value(reverse_folder):
    """

    :param reverse_folder: 反编译后的文件夹
    :return: 所有channel
    """
    # 设置要查找的文本
    text_umeng_channel = "UMENG_CHANNEL"
    umeng_channel = []

    for rfn in reverse_folder:
        manifest = os.path.join(version_catalogue, rfn, 'AndroidManifest.xml')  # 拼接出AndroidManifest.xml路径
        # 友盟渠道号
        umeng_channel.append(handling(manifest, text_umeng_channel))
    # print(umeng_channel)
    return umeng_channel


# def output_test_results():
#     # 获取apk名称和友盟渠道号
#     apkname, reverse_folder = decompiler(version_catalogue)
#     umeng_channel_value = get_apk_umeng_value(reverse_folder)
#     test_result = {"APKNAME": apkname, "UMENG_CHANNEL": umeng_channel_value
#                    }
#     frame = DataFrame(test_result, columns=["APKNAME", "UMENG_CHANNEL"])
#     print(frame)
#     return frame


def check_channel_all(file):
    """
    比较所有的差异
    :param file: 产品需求channel文档
    :return:
    """
    with open(file, 'r+') as f:
        line = [line.strip() for line in f.readlines()]
    apkname, reverse_folder = decompiler(version_catalogue)
    time.sleep(10)
    actual = get_apk_umeng_value(reverse_folder)  # 实际获取到的channel
    print('实际获取到的channel：%s 个\n  -> %s' % (len(actual), actual) + '\n')
    demand = line  # 需求channel
    print('打包需求的channel：%s 个\n  -> %s ' % (len(demand), demand) + '\n')
    diff = []
    for i in demand:
        if i not in actual:
            diff.append(i)
    if not diff:
        print("channel一致")
    else:
        print('没有创建的channel：\n  -> %s ' % diff + '\n')


check_channel_all("/Users/naoli/Desktop/channel.txt")


