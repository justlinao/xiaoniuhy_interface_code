# -*- coding: UTF-8 -*-
import base64
from io import BytesIO
import gzip
from io import StringIO
import binascii


def gzip_uncompress(data):
    """
    先使用base64解码，然后再对gzip压缩过的数据进行解码，使用到的是 from io import BytesIO
    import gzip
    """
    data = base64.b64decode(data.encode('utf-8'))
    # print(data)  # 解码
    buff = BytesIO(data)  # gzip解码
    data = gzip.GzipFile(fileobj=buff)
    data = data.read().decode('utf-8')
    return data


def gzip_compress(data):
    """
    通过gzip对数据流进行加密 再进行base64加密
    :param data: 需要加密的数据
    :return: data
    """
    data = data.encode("utf-8")
    buf = BytesIO()
    f = gzip.GzipFile(mode='wb', fileobj=buf)
    try:
        f.write(data)
    finally:
        f.close()
    data = buf.getvalue()   # gzip加密后的数据
    data = base64.b64encode(data).decode("utf-8")  # base64加密后的数据 并把bytes类型转换成str
    return data


if __name__ == '__main__':
    data = "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"
    read_data = gzip_uncompress(data)
    print("解码后的数据： {}".format(read_data))
    a = gzip_compress(read_data)
    print("加密后的数据： {}".format(a))
    b = gzip_uncompress(a)
    print("再次解密后的数据：{}".format(b))
