# -*- coding: utf-8 -*-

#
# Interview task for hellowisp.com
# Author: KALINOWSKI PAWEL <kalinowskipawel@yahoo.com>
#

from fastapi import APIRouter, Body, Depends
from fastapi import Depends, Body, Query, Path, FastAPI, HTTPException, File, UploadFile, BackgroundTasks, Security

from modules.specialmath.model import SpecialMathStatus, SpecialMathResponse, SpecialMathIn

from . import service

router = APIRouter()

@router.get("/specialmath/{number}", 
    response_model = SpecialMathResponse,
    responses = {},
    tags = ["math"],
    summary = "Calculate special math formula"
)
async def specialmath(
    number: int = Path(..., title = "The number that you want to calculate", ge = 0, le = 100000),
) -> SpecialMathResponse:
    # Get value of special math
    value = await service.special_math(number)

    # TODO:
    # Implement caching solution
    cached = False 
    
    if value is not None:
        return SpecialMathResponse(result = SpecialMathStatus.success, value = value, cached = cached) 

    return SpecialMathResponse(result = SpecialMathStatus.failed, cached = cached)