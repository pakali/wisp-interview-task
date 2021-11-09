# -*- coding: utf-8 -*-

#
# Interview task for hellowisp.com
# Author: KALINOWSKI PAWEL <kalinowskipawel@yahoo.com>
#

from starlette.middleware.base import BaseHTTPMiddleware

class QueryLimitMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, throttle = 100):
        super().__init__(app)
        self.throttle = throttle

    async def dispatch(self, request, call_next):
        
        # TODO:
        # We can build query limiter here with redis

        response = await call_next(request)
        return response
