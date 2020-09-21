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
    data = "H4sIAAAAAAAAAKtWKihKTc4syCxJLMnMz1OyijbQM9AZQThWR6k8NbEkI7UopLIgVclK6eXsFUo6qKESb5Qx8gJmpGFgQkhJLEkszi8tSgalg6LElMQicErIT0pMyszJLKnETARATRn5ualBiZnArJOWmFOcCjQltTi5KLMAkp2Uns1Z9Wzu0ic7ljzd0P9s+rYnO3qf7Jn1ZEc3JJnl5CfD8p2xoZ6RgaWBhZmOoZGhnpmRmYGlCdD44tSiMmDazMwFusnQ1NLS0NDcwMAAKA5MmqXFQAvys4HmZBYHZ+SXK1mVFJWm1gIAwfpJdtQDAAA="
    read_data = gzip_uncompress(data)
    print("解码后的数据： {}".format(read_data))
    a = gzip_compress(read_data)
    print("加密后的数据： {}".format(a))
    b = gzip_uncompress(a)
    print("再次解密后的数据：{}".format(b))
