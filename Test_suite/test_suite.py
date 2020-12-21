# -*- coding: UTF-8 -*-

import unittest
import requests
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from Public.log import get_log
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from HTMLTestRunner import HTMLTestRunner
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.utils import parseaddr, formataddr

# print(sys.path)


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def send_email(file_new):
    msg = MIMEMultipart()

    # 发送邮箱服务器
    smtpsever = 'smtp.qq.com'
    # 发送邮箱用户 登录使用
    user = '913896561@qq.com '
    password = 'inmwizhzuzztbdcf'
    # 发送用户
    sender = '913896561@qq.com'
    # 接收用户
    receiver = '205585244@qq.com'
    # 发送主题
    subject = 'API_Test_Report'

    # 编写HTML 类型的邮件正文
    msg['Subject'] = Header(subject, 'utf-8')
    txt = MIMEText('这是API自动化测试报告，请使用浏览器打开附件并点击详情查看测试结果\n如有问题请及时联系', 'plain', 'utf-8')
    msg.attach(txt)
    msg['From'] = _format_addr(u'李闹<%s>' % user)
    msg['to'] = _format_addr(receiver)

    # 发送附件
    sendfile = open(file_new, 'rb').read()  # 获取报告
    text_att = MIMEText(sendfile, 'html', 'uft-8')  # 添加附件
    text_att["Content-Type"] = 'application/octet-stream'  # 附件类型
    text_att.add_header('Content-Disposition', 'attachment', filename='test_result.html')
    msg.attach(text_att)

    # 直接发送邮件（smtplib模块 基本使用格式）
    smtp = smtplib.SMTP()
    smtp.connect(smtpsever)
    smtp.login(user, password)
    smtp.sendmail(sender, receiver.split(','), msg.as_string())
    get_log().info('邮件发送成功')
    smtp.quit()


def get_report(test_report):
    lists = os.listdir(test_report)  # 列出目录的下所有文件和文件夹保存到list
    lists.sort(key=lambda fn: os.path.getmtime(test_report + "/" + fn))  # 按时间排序
    file_new = os.path.join(test_report, lists[-1])  # 获取最新的文件保存到file_new
    # print(file_new)
    return file_new


def send_qyweixin(counts, success_counts, fail_counts, fail_list):
    get_test_log = get_report(path + r'/Log')
    with open(get_test_log, 'r') as f:  # 读取最新的接口请求日志发送到指定群里
        lines = f.readlines()
        result = "".join(lines)  # 列表转成str
        url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=87a28e87-88a4-4a1c-90c9-41dc09e97204"
        headers = {"Content-Type": "text/plain"}
        # s = ("执行%s个接口, 成功数%s, 失败数%s，" % (counts, success_counts, fail_counts))
        if fail_counts == 0:  # 如何没有失败的接口 就不展示失败接口
            data = {
                "msgtype": "markdown",  # 消息类型，此时固定为markdown
                "markdown": {
                    "content":
                        '接口测试结果' + '\n' +
                        # result +
                        '\n' + '执行接口数：' + '<font color=\"info\">%s</font>' % counts +  # info 绿色，comment灰色， warning黄色
                        '\n' + '成功数：' + '<font color=\"info\">%s</font>' % success_counts +
                        '\n' + '成功率' + '<font color=\"info\">%s</font>' % (success_counts / counts * 100) +
                        '<font color=\"info\">%s</font>' % '%'
                    # "mentioned_list": ["@all"]  # @所有人
                }
            }
        else:
            data = {
                "msgtype": "markdown",  # 消息类型，此时固定为markdown
                "markdown": {
                    "content":
                        '接口测试结果' + '\n' +
                        # result +
                               '\n'+'执行接口数：'+'<font color=\"info\">%s</font>' % counts +     # info 绿色，comment灰色， warning黄色
                               '\n'+'成功数：'+'<font color=\"info\">%s</font>' % success_counts +
                               '\n'+'失败数：'+'<font color=\"warning\">%s</font>' % fail_counts +
                               '\n'+'失败接口：'+'\n'+'<font color=\"warning\">%s</font>' % fail_list +
                               '\n' + '成功率' + '<font color=\"warning\">%s</font>' % (success_counts / counts * 100) +
                               '<font color=\"warning\">%s</font>' % '%'
                    # "mentioned_list": ["@all"]  # @所有人
                }
            }
        r = requests.post(url, headers=headers, json=data)
        return r


if __name__ == '__main__':
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 当前目录最上级
    print(path)
    case_path = path + r'/TestCase'
    print(case_path)
    discover = unittest.defaultTestLoader.discover(case_path,
                                                   pattern="test*.py",
                                                   top_level_dir=None)   # 测试模块的顶层目录，如果没有顶层目录，默认为None
    with open(path+r'\TestReport\HTMLTestRunner.html', 'wb+') as f:
        runner = HTMLTestRunner(stream=f,             # 进入f 这个文件里
                                title='API Test Report',   # 报告 标题
                                description='generated by HTMLTestRunner.',  # 描述
                                verbosity=2     # 报告的信息程度 一般分为0 - 6级
                                )
        test_result = runner.run(discover)
    # test_result = unittest.TextTestRunner().run(discover)  # 执行case
    counts = discover.countTestCases()  # 总个数
    success_counts = counts - int(len(test_result.failures))  # 成功个数
    fail_counts = int(len(test_result.failures))  # 失败个数
    fail_list = []  # 储存失败接口
    if test_result.failures:
        for case, reason in test_result.failures:
            fail_list.append(case.id() + '\n')
    fail_list = ''.join(fail_list)
    # get_report1 = get_report(path+r'\TestReport')  # 获取最新的测试报告
    send_qyweixin(counts, success_counts, fail_counts, fail_list)

# send_email(get_report)
