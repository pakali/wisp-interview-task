# -*- coding: utf-8 -*-

#
# Interview task for hellowisp.com
# Author: KALINOWSKI PAWEL <kalinowskipawel@yahoo.com>
#

import redis

def get_connection():
    redis_pool = redis.ConnectionPool(host='redis', port=6379, db=0)
    session = redis.Redis(connection_pool=redis_pool)

    return session