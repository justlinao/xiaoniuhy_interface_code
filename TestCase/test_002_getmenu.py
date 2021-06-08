# -*- coding: UTF-8 -*-

import unittest
from xiaochengxu_interface.getMenu import get_menu
from Public.log import get_log
from Public.get_env_yaml import read_config


class GetMenu(unittest.TestCase):
    def setUp(self):
        pass

    def test_getmenu(self):
        self.get_menu = get_menu()
        get_log().info('获取底部菜单接口--->status_code：{},  请求时长：{}'.format(self.get_menu[1], self.get_menu[0]))
        try:
            self.assertEquals(self.get_menu[1], 200, '请求失败，status_code：%s' % self.get_menu[1])
            self.assertLess(self.get_menu[0], read_config(), '请求超时，实际请求时长%s毫秒' % self.get_menu[0])
        except AssertionError:
            raise AssertionError

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
