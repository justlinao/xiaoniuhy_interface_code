import os
import sys
import shutil
import requests
import time
from pandas import DataFrame, Series


# ���ð�׿�����汾����Ŀ¼,ApkTool�ɲ���
version_catalogue = r"/Users/naoli/Desktop/60174-60921"
ApkTool = r"/Users/naoli/Desktop/apktool.jar"
now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

# apktool.jar��ַ
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

# ����������apktool.jar�����빤��
if os.path.exists(os.path.join(version_catalogue, 'apktool.jar')):
    print(" ->{0} Has found a decompiler apktool.jar.\n".format(version_catalogue))
elif os.path.isfile(ApkTool):
    shutil.copy(ApkTool, version_catalogue)
else:
    with open('apktool.jar', 'wb') as atool:
        print(" -> The Computer is not exists apktools.jar,Will begining Download Apktools.jar......")
        atool.write(requests.get(apktool_download_url).content)

start_time = time.time()


# ������android apk
def decompiler(vdir):
    """

    :param vdir: ���apk���ļ���
    :return: apk�ļ���reverse_apk_folder��������ļ�
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
    time.sleep(10)  # �ȴ��������
    reverse_apk_folder = [opf for opf in os.listdir(vdir) if os.path.isdir(opf)]
    print("-------------------------------------------------------------------")
    print(" -> {0} Finish Apk decompiling.".format(now))
    print(" -> Total: \033[1;32;44m {0} \33[0m Apk Floder. ".format(len(reverse_apk_folder)))
    return vapk, reverse_apk_folder


# ����AndroidManifest.xml�ļ�
def handling(filename, text):
    """

    :param filename: AndroidManifest.xml�ļ�
    :param text: ������ֶ�/channel
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
            # ʹ��strip����"/>//--�������ַ�
            textual_value = value.strip('"/>// --')
    return textual_value


# ������������apk�ļ��У�ͨ��AndroidManifest.xml�ļ���ȡ������
def get_apk_umeng_value(reverse_folder):
    """

    :param reverse_folder: ���������ļ���
    :return: ����channel
    """
    # ����Ҫ���ҵ��ı�
    text_umeng_channel = "UMENG_CHANNEL"
    umeng_channel = []

    for rfn in reverse_folder:
        manifest = os.path.join(version_catalogue, rfn, 'AndroidManifest.xml')  # ƴ�ӳ�AndroidManifest.xml·��
        # ����������
        umeng_channel.append(handling(manifest, text_umeng_channel))
    # print(umeng_channel)
    return umeng_channel


# def output_test_results():
#     # ��ȡapk���ƺ�����������
#     apkname, reverse_folder = decompiler(version_catalogue)
#     umeng_channel_value = get_apk_umeng_value(reverse_folder)
#     test_result = {"APKNAME": apkname, "UMENG_CHANNEL": umeng_channel_value
#                    }
#     frame = DataFrame(test_result, columns=["APKNAME", "UMENG_CHANNEL"])
#     print(frame)
#     return frame


def check_channel_all(file):
    """
    �Ƚ����еĲ���
    :param file: ��Ʒ����channel�ĵ�
    :return:
    """
    with open(file, 'r+') as f:
        line = [line.strip() for line in f.readlines()]
    apkname, reverse_folder = decompiler(version_catalogue)
    time.sleep(10)
    actual = get_apk_umeng_value(reverse_folder)  # ʵ�ʻ�ȡ����channel
    print('ʵ�ʻ�ȡ����channel��%s ��\n  -> %s' % (len(actual), actual) + '\n')
    demand = line  # ����channel
    print('��������channel��%s ��\n  -> %s ' % (len(demand), demand) + '\n')
    diff = []
    for i in demand:
        if i not in actual:
            diff.append(i)
    if not diff:
        print("channelһ��")
    else:
        print('û�д�����channel��\n  -> %s ' % diff + '\n')


check_channel_all("/Users/naoli/Desktop/channel.txt")


