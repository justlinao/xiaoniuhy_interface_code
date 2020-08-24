"""
只是用ddt进行数据驱动
"""
import unittest
from xiaoniu_interface.login import login
import ddt
from Public.log import get_log

@ddt.ddt
class Login(unittest.TestCase):
    def setUp(self):
        pass

    @ddt.data(['18111111111', '1234'], ['18111111112', '9527'])
    @ddt.unpack
    def test_login(self, A, B):
        self.login = login(A, B)
        self.assertEquals(self.login, 200, '与预期不符合用例失败')
        get_log().info('登录接口请求结果%s' % self.login)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()

