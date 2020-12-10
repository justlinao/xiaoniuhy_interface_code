# coding=utf-8
"""
只使用excel进行数据驱动
"""
import unittest
from xiaoniu_interface.my_test import my_login
from Public.log import get_log
from Public.readexcel import ReadExcel


class Login(unittest.TestCase):
    def setUp(self):
        pass

    def test_excel_login(self):
        rows = ReadExcel().get_rows()  # 获取表单的所有行
        print(rows)
        for i in range(rows):
            data = ReadExcel().get_row_value(i+2)  # 获取每一行的数据，返回的是list
            print(data)
            if data[0] != None:
                self.login = my_login(data[0], data[1])  # 获取具体单元格的数据入参
                # get_log().info("账号：{} 密码：{}".format(data[0], data[1]))
                get_log().info('登录接口请求结果%s' % self.login)
                self.assertEqual(self.login[0], data[2])

            else:
                break

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
