# -*- coding: utf-8 -*-

#
# Interview task for hellowisp.com
# Author: KALINOWSKI PAWEL <kalinowskipawel@yahoo.com>
#
import os

from fastapi import FastAPI

from modules import api

from middlewares.query_limit import QueryLimitMiddleware
from middlewares.process_time import ProcessTimeMiddleware
from middlewares.cors import CORSMiddleware

"""
Application initialization variables
"""
stage = os.environ.get('STAGE', None)

"""
Initialize FastAPI
"""
app = FastAPI(
    title = "Special Math API",
    description = "Implementation of interview task in Python, ensuring someone can call through a REST endpoint math formula described at interview task.",
    root_path = f"/{stage}" if stage else "/"
)

"""
Initialize middlewares
"""
app.add_middleware(
    CORSMiddleware,
    allow_origins = [
        "http://localhost",
    ],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

app.add_middleware(
    ProcessTimeMiddleware,
)

app.add_middleware(
    QueryLimitMiddleware,
    throttle = 100
)

"""
Initialize API router
"""
app.include_router(api.router)