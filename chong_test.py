# -*- coding: UTF-8 -*-
import requests
from multiprocessing import Pool
import json

url = "http://stockpage.10jqka.com.cn/000333/#dzjy"
headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Content-Type": "text/html",
        "Host": "stockpage.10jqka.com.cn",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
    }

re = requests.get(url=url, headers=headers)
print(re.status_code, re.text)