# -*- coding: utf-8 -*-

#
# Interview task for hellowisp.com
# Author: KALINOWSKI PAWEL <kalinowskipawel@yahoo.com>
#

"""
Default store class
"""
class Store:
    redis = None

"""
Store object
"""
store = Store()

"""
Store async function can be used for dependency injections
"""
async def get_store() -> Store:
    return store
