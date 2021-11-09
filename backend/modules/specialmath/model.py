# -*- coding: utf-8 -*-

#
# Interview task for hellowisp.com
# Author: KALINOWSKI PAWEL <kalinowskipawel@yahoo.com>
#

from pydantic import BaseConfig, BaseModel, EmailStr, Field
from typing import List, Optional

from enum import Enum

"""
Information about status result
"""
class SpecialMathStatus(str, Enum):
    success = "success"
    failed = "failed"

"""
Special Math Response
"""
class SpecialMathResponse(BaseModel):
    """
    Result status
    """
    result: Optional[SpecialMathStatus] = SpecialMathStatus.failed
    """
    Value is string because BigInt cant be represented in Json output
    """
    value: Optional[str] = None
    """
    Information about cached output
    """
    cached: Optional[bool] = None

"""
Special Math Input
"""
class SpecialMathIn(BaseModel):
    """
    Number provided by user
    """
    number: Optional[int] = 1