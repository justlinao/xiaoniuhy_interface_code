import requests
import json
from Public.req_header import login_headers
login_headers = login_headers()


def startlive():
    url = 'http://qx-fat.qianshi188.com/gateway/room/liveroom/startlive'
    data = {'roomId': 'eeeee', 'customerId': '06d0ce55dac24c2eaf2f6e335804fc28',
            'coverUrl': 'http://00.minipic.eastday.com/20170525/20170525151413_87ad5f4c0d7a5798892bdf21d6323cf6_6.jpeg',
            }
    re = requests.post(headers=login_headers, url=url, data=json.dumps(data))
    print(re.status_code, re.text)
    re = json.loads(re.text)
    print(re)
    # roomId = re['data']['roomId']
    # customerId = re['data']['customerId']
    # liveDetailId = re['data']['liveDetailId']
    # return roomId, customerId, liveDetailId


startlive()
