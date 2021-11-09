# -*- coding: utf-8 -*-

#
# Interview task for hellowisp.com
# Author: KALINOWSKI PAWEL <kalinowskipawel@yahoo.com>
#

import starlette.middleware.cors

class CORSMiddleware(starlette.middleware.cors.CORSMiddleware):
    pass