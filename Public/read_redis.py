# -*- coding: UTF-8 -*-
import redis


class TestString:
    """
    set --设置值
    get --获取值
    mset --设置多个键值对
    mget --获取多个键值对
    append --添加字符串
    del --删除
    incr/decr -- 增加/减少 1
    """

    def __init__(self):
        pool = redis.ConnectionPool(host="r-uf61z84u733tugqsuj.redis.rds.aliyuncs.com", port=6379, db=2,
                                    password='fzcfQwuMH2q')
        self.r = redis.Redis(connection_pool=pool)

    def test_set(self, key, value):
        """
        设置string类型的value
        :return: 返回设置的结果 True
        """
        rest = self.r.set(key, value)
        # print(rest)
        return rest

    def test_get(self, key):
        rest = self.r.get(key).decode()
        # print(rest)
        return rest

    def test_mset(self, data):
        """
        data 是个字典data={key：value，key1：value1}
        mset --设置多个键值对
        :return:返回设置的结果 True
        """
        rest = self.r.mset(data)
        print(rest)
        return rest

    def test_mget(self, l):
        """
        l,传入的就是一个列表l=[key,key1]
        mget --获取多个键值对
        :return:返回一个列表
        """
        list = []
        rest = self.r.mget(l)
        for i in rest:
            print(i.decode())
            list.append(i)
        return list

    def test_del(self, key):
        """
        del 删除
        :return:
        """
        rest = self.r.delete(key)
        print(rest)

        return rest


# if __name__ == '__main__':
#     TestString().test_set()
#     TestString().test_get()
#     TestString().test_mset()
#     TestString().test_mget()
#     TestString().test_del()


class TestList:
    """
    lpush/rpush --从左/右插入数据
    lrange -- 获取指定长度的数据
    ltrim -- 截取一定长度的数据
    lpop/rpop -- 移除最左/右的元素并返回
    lpushx/rpushx -- key存在的时候才插入数据，不存在不做任何处理
    """

    def __init__(self):
        pool = redis.ConnectionPool(host="r-uf61z84u733tugqsuj.redis.rds.aliyuncs.com", port=6379, db=2,
                                    password='fzcfQwuMH2q')
        self.r = redis.Redis(connection_pool=pool)

    def test_lget(self, key, index):
        """
        获取指定索引下的值
        :return:
        """
        result = self.r.lindex(key, index).decode()
        # print(result)
        return result

    def test_push(self, key, value_tuple):
        """
        lpush/rpush --从左/右插入数据
        lrange -- 获取指定长度的数据
        :return:
        """

        reset = self.r.lpush(key, *value_tuple)
        print(reset)
        reset = self.r.lrange(key, 0, -1)
        print(reset)

    def test_pop(self, key):
        """
        lpop/rpop -- 移除最左/右的元素并返回
        :return:
        """
        rest = self.r.lpop(key)
        print(rest)

        reset = self.r.lrange(key, 0, -1)
        print(reset)


if __name__ == '__main__':
    pass


class TestSet:
    """
    sadd/srem --添加/删除元素
    sismember --判断是否为set的一个元素
    smembers --返回该集合的所有成员
    sdiff --返回一个集合与其他集合的差异
    sinter --返回几个集合的交集
    sunion --返回几个集合的并集
    """
    def __init__(self):
        pool = redis.ConnectionPool(host="r-uf61z84u733tugqsuj.redis.rds.aliyuncs.com", port=6379, db=2,
                                    password='fzcfQwuMH2q')
        self.r = redis.Redis(connection_pool=pool)

    def test_sadd(self, key, list):
        """
        sadd/srem --添加/删除元素
        :return:
        """
        rest = self.r.sadd(key, *list)
        print(rest)
        rest = self.r.smembers(key)
        print(rest)

    def test_srem(self, key, value):
        """
        sadd/srem --添加/删除元素
        :return:
        """
        rest = self.r.srem(key, value)
        print(rest)
        rest = self.r.smembers(key)
        print(rest)

    def test_sinter(self):
        """
        sinter --返回几个集合对象的交集
        sunion --返回几个集合对象的并集
        :return:
        """
        rest = self.r.sunion('zoo2', 'zoo3')
        print(rest)
        rest = self.r.sinter('zoo2', 'zoo3')
        print(rest)


if __name__ == '__main__':
    pass


class TestHash:
    """
    hset/hget --设置/获取散列值
    hmset/hmget --设置/获取多对散列值
    hsetnx --如果散列已经存在，则不设置
    hkeys/hvals --返回所有Keys/Values
    hlen -- 返回散列包含域
    """
    def __init__(self):
        pool = redis.ConnectionPool(host="r-uf61z84u733tugqsuj.redis.rds.aliyuncs.com", port=6379, db=2,
                                    password='fzcfQwuMH2q')
        self.r = redis.Redis(connection_pool=pool)

    def test_set(self):
        """
        hset/hget --设置/获取散列值
        :return:
        """
        reset = self.r.hset('stu:xxx01', 'name', 'Amy')
        print(reset)
        reset = self.r.hexists('stu:xxx01', 'name')
        print(reset)

        reset = self.r.hget('stu:xxx01', 'name')
        print(reset)

    def test_mset(self):
        """
        hmset/hmget --设置/获取多对散列值
        :return:
        """
        m = {
            'name': 'Bob',
            'age': 21,
            'grade': 98
        }
        rest = self.r.hmset('stu:xxx03', m)
        print(rest)
        rest = self.r.hkeys('stu:xxx03')
        print(rest)


if __name__ == '__main__':
    pass


