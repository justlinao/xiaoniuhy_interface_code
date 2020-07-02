import requests
import json
from Public.req_header import headers
from Public.get_env_yaml import read_config
from xiaoniu_interface.start_live import startlive
headers = headers()
env = read_config()
startlive = startlive()  # 获取关播需要的参数
# print(startlive) 返回的是一个元组


def endlive():
    url = 'http://qx-fat.qianshi188.com/gateway/room/liveroom/endlive'
    data = {'roomId': startlive[0], 'customerId': startlive[1]
            , "liveDetailId": startlive[2]}
    re = requests.post(headers=headers, url=url, data=json.dumps(data))
    print(re.status_code, re.text)


endlive()
