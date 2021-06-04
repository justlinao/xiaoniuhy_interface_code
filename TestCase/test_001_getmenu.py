# -*- coding: UTF-8 -*-

import unittest
from xiaochengxu_interface.getMenu import get_menu
from Public.log import get_log


class GetMenu(unittest.TestCase):
    def setUp(self):
        pass

    def test_getmenu(self):
        self.get_menu = get_menu()
        get_log().info('获取底部菜单接口--->status_code：{},  请求时长：{}'.format(self.get_menu[0], self.get_menu[1]))
        try:
            self.assertEquals(self.get_menu[0], 200, '请求失败')
            self.assertLess(self.get_menu[1], 90, '请求超时，实际请求时长%s毫秒' % self.get_menu[1])
        except AssertionError:
            raise AssertionError

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
