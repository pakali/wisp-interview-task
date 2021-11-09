# -*- coding: utf-8 -*-

#
# Interview task for hellowisp.com
# Author: KALINOWSKI PAWEL <kalinowskipawel@yahoo.com>
#
from fastapi.testclient import TestClient

from main import app

import logging
import pytest

client = TestClient(app)

def special_math(n : int = 0) -> int:
    if n == 0: return 0
    elif n == 1: return 1
    return n + special_math(n - 1) + special_math(n - 2)

def test_special_math_endpoint():
    response = client.get("/specialmath/1", headers={})
    assert response.status_code == 200

def test_special_math_validation_min():
    response = client.get("/specialmath/-1", headers={})
    assert response.status_code == 422
    assert response.json() == {"detail":[{"loc":["path","number"],"msg":"ensure this value is greater than or equal to 0","type":"value_error.number.not_ge","ctx":{"limit_value":0}}]}

def test_special_math_validation_max():
    response = client.get("/specialmath/100001", headers={})
    assert response.status_code == 422
    assert response.json() == {"detail":[{"loc":["path","number"],"msg":"ensure this value is less than or equal to 100000","type":"value_error.number.not_le","ctx":{"limit_value":100000}}]}

def test_special_math_validation_alpha():
    response = client.get("/specialmath/abc", headers={})
    assert response.status_code == 422
    assert response.json() == {'detail': [{'loc': ['path', 'number'], 'msg': 'value is not a valid integer', 'type': 'type_error.integer'}]} != {'detail': [{'ctx': {'limit_value': 100000}, 'loc': ['path', 'number'], 'msg': 'ensure this value is less than or equal to 100000', 'type': 'value_error.number.not_le'}]}

def test_special_math_validation_special():
    response = client.get("/specialmath/@!", headers={})
    assert response.status_code == 422
    assert response.json() == {'detail': [{'loc': ['path', 'number'], 'msg': 'value is not a valid integer', 'type': 'type_error.integer'}]} != {'detail': [{'ctx': {'limit_value': 100000}, 'loc': ['path', 'number'], 'msg': 'ensure this value is less than or equal to 100000', 'type': 'value_error.number.not_le'}]}

@pytest.mark.parametrize("n", [n for n in range(30)])
def test_special_math_results(n):
    result = special_math(n)

    response = client.get("/specialmath/%d" % (n), headers={})
    
    assert response.status_code == 200
    assert response.json().get("result") == "success"
    assert response.json().get("value") == str(result)
