# -*- coding: utf-8 -*-

#
# Interview task for hellowisp.com
# Author: KALINOWSKI PAWEL <kalinowskipawel@yahoo.com>
#

from starlette.middleware.base import BaseHTTPMiddleware

import time

class ProcessTimeMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        response.headers["X-Process-Time"] = str(process_time)
        return response
