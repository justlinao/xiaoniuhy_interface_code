# -*- coding: UTF-8 -*-
import requests
from xiaoniu_interface import forbidden_save
code = forbidden_save.forbidden_save()
print(code)
text = "举报接口执行结果：" + str(code)
print(text)
sess = requests.session()
url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=87a28e87-88a4-4a1c-90c9-41dc09e97204"
headers = {"Content-Type": "text/plain"}
s = "What do you want to say? "
data = {
      "msgtype": "text",
      "text": {
         "content": text,
      }
   }
r = sess.post(url, headers=headers, json=data)

print(r.text)
