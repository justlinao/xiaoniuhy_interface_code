# -*- coding: UTF-8 -*-
import unittest
from xiaochengxu_interface.task import get_task
from Public.log import get_log
from Public.get_env_yaml import read_config


class MyTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_task(self):
        self.get_task = get_task()
        get_log().info('获取底部菜单接口--->status_code：{},  请求时长：{}'.format(self.get_task[1], self.get_task[0]))
        try:
            self.assertEquals(self.get_task[1], 200, '请求失败')
            self.assertLess(self.get_task[0], read_config(), '请求超时，实际请求时长%s毫秒' % self.get_task[0])
        except AssertionError:
            raise AssertionError

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()