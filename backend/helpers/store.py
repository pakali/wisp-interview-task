# -*- coding: utf-8 -*-

#
# Interview task for hellowisp.com
# Author: KALINOWSKI PAWEL <kalinowskipawel@yahoo.com>
#

from helpers.connect import store
from helpers.redis import get_connection as redis_connection

store.redis = redis_connection()