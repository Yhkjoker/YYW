import redis


class RedisConnection(object):
    def __init__(self):
        pool = redis.ConnectionPool(host='47.107.238.126', port=6379,
                                    decode_responses=True)  # host是redis主机，需要redis服务端和客户端都起着 redis默认端口是6379
        self._r = redis.Redis(connection_pool=pool)

    def get(self):
        return self._r


REDIS = RedisConnection().get()
