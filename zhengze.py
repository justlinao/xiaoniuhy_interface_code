# -*- coding: UTF-8 -*-
import re
# with open(r"C:\Users\linao\Desktop\language\EnglishTransformationEnum.txt", 'r+', encoding='utf-8') as f:
#     file = f.read()
#     print(file)
#     patten = re.compile(', "(.*?)"\)', re.S)  # 转义符 \，
#     items = re.findall(patten, file)
#     print(items)
result = [('<test_001_getmenu.GetMenu testMethod=test_getmenu>', 'Traceback (most recent call last):\n  File "/Users/naoli/Desktop/xiaoniuhy_interface_code/TestCase/test_001_getmenu.py", line 17, in test_getmenu\n    self.assertLess(self.get_menu[1], 10, \'超时，实际用时%s\' % self.get_menu[1])\nAssertionError: 96 not less than 10 : 超时，实际用时96\n\nDuring handling of the above exception, another exception occurred:\n\nTraceback (most recent call last):\n  File "/Users/naoli/Desktop/xiaoniuhy_interface_code/TestCase/test_001_getmenu.py", line 19, in test_getmenu\n    raise AssertionError\nAssertionError\n')]
# patten = re.compile('AssertionError： "(.*)"During',)
result = str(result)
items = re.findall(r'AssertionError: (.*)Du', result, re.S)
items = str(items)
print(items)