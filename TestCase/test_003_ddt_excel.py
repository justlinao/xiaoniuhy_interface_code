# coding=utf-8
"""
使用ddt 结合excel进行数据驱动
"""
import unittest
from xiaoniu_interface.my_test import my_login
from Public.log import get_log
from Public.readexcel import ReadExcel
import ddt
data = ReadExcel.get_rows_value()

@ddt.ddt
class Login(unittest.TestCase):
    def setUp(self):
        pass

    @ddt.data(*data)
    def test_ddt_excel_login(self, data):
        user, password, except_code = data  # ddt中要把数据和参数对应起来 这里的data [test,123456,200]
        self.login = my_login(user, password)  # 获取具体单元格的数据入参
        self.assertEqual(self.login[0], except_code, "与预期结果不一致，用例失败")
        get_log().info("账号：{} 密码：{}".format(user, password))
        get_log().info('登录接口请求结果%s' % self.login)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
