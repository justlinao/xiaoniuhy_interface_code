# -*- coding: UTF-8 -*-

import unittest
from xiaochengxu_interface.homeGuessList import home_guess_list
from Public.log import get_log


class HomeGuessList(unittest.TestCase):
    def setUp(self):
        pass

    def test_homeguesslist(self):
        self.homeguesslist = home_guess_list()
        get_log().info('获取猜你喜欢%s' % self.homeguesslist)
        self.assertEquals(self.homeguesslist, 'success', '与预期不符合用例失败')

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
