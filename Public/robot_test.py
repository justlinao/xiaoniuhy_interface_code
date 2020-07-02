import requests

url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=87a28e87-88a4-4a1c-90c9-41dc09e97204"
headers = {"Content-Type": "text/plain"}
s = "What do you want to say? "
data = {
      "msgtype": "text",
      "text": {
         "content": s,
      }
   }
r = requests.post(url, headers=headers, json=data)
print(r.text)
