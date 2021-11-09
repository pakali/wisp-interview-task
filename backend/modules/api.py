# -*- coding: utf-8 -*-

#
# Interview task for hellowisp.com
# Author: KALINOWSKI PAWEL <kalinowskipawel@yahoo.com>
#

from fastapi import APIRouter

from .specialmath.crud import router as specialmath_router

router = APIRouter()

router.include_router(specialmath_router)