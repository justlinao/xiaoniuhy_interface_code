# -*- coding: UTF-8 -*-
import requests
import re
from multiprocessing import Pool
import json
import codecs


def get_maoyan(url, header):

    response = requests.get(url, header)
    if response.status_code == 200:
        print(response.text)
        return response.text
    return None


def get_one_page(html):
    patten = re.compile('<dd>.*?board-index.*?">(\d+)</i>.*?title="(.*?)".'
                        '*?data-src="(.*?)".*?star">(.*?)</p >.*?releasetime">(.*?)</p >', re.S)
    items = re.findall(patten, html)
    for item in items:
        yield {
            'index': item[0],
            'name': item[1],
            'img': item[2],
            'star': item[3].strip()[3:],  # strip()取值，[3：]切片index2以后的
            'time': item[4].strip()[5:]
        }
    return items


def write_to_file(file):
    with open('1.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(file, ensure_ascii=False) + '\n')
        f.close()


def main(offset):
    header = {
        'user-agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    url = 'https://maoyan.com/board/4?offset=' + str(offset)
    for item in get_one_page(get_maoyan(url, header)):
        print(item)
        write_to_file(item)


if __name__ == '__main__':
    pool = Pool()
    pool.map(main, [i*10 for i in range(1)])
