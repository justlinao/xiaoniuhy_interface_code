# -*- coding: UTF-8 -*-

import unittest
from xiaochengxu_interface.homeGuessList import home_guess_list
from Public.log import get_log
from Public.get_env_yaml import read_config


class HomeGuessList(unittest.TestCase):
    def setUp(self):
        pass

    def test_homeguesslist(self):
        self.homeguesslist = home_guess_list()
        get_log().info('获取猜你喜欢--->status_code：{},  请求时长：{}'.format(self.homeguesslist[1], self.homeguesslist[0]))
        try:
            self.assertEquals(self.homeguesslist[1], 200, '请求失败')
            self.assertLess(self.homeguesslist[0], read_config(), '请求超时，实际请求时长%s毫秒' % self.homeguesslist[0])
        except AssertionError:
            raise AssertionError

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
