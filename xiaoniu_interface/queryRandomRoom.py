# -*- coding: UTF-8 -*-
import requests
import json
from Public.req_header import json_headers


def randomroom():
    url = "http://qx-fat.qianshi188.com/gateway/room/liveroom/queryrandomroom"
    data = ""
    headers = json_headers()
    re = requests.post(url=url, data=json.dumps(data), headers=headers)
    re = json.loads(re.text)
    # print(re)
    # print("直播状态为：", re['data']['liveStatus'], "直播间状态（0-未开播，1-直播中）")
    roomid = re['data']['roomId']
    print("推荐接口返回的roomid：", roomid)

    return re['data']['liveStatus'], roomid


k = 10
j = 0
for i in range(k):
    re = randomroom()
    if re[0] == 1:
       j += 1
    # print("第 %s 次" % j)
# print("获取推荐主播 %s 次" % k)
print("获取到开播主播 %s 次 " % j)
print("获取到关播主播 %s 次" % (k-j))


