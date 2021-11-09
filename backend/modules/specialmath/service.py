# -*- coding: utf-8 -*-

#
# Interview task for hellowisp.com
# Author: KALINOWSKI PAWEL <kalinowskipawel@yahoo.com>
#

async def fib(n : int) -> int:
    """
    Used to calculate fibonacii sequence values
    """
    v1, v2, v3 = 1, 1, 0   
    for rec in bin(n)[3:]: 
        calc = v2 * v2
        v1, v2, v3 = v1 * v1 + calc, (v1 + v3) * v2, calc + v3 * v3
        if rec == '1': v1, v2, v3 = v1 + v2, v1, v2
    return v2

async def special_math(n : int = 0) -> int:
    """
    Using Wolfdieter Lang solution by N.J.A Sloane encyclopedia:
    Apply partial sum operator twice to Fibonacci numbers. 
    https://oeis.org/A001924
    """
    return await fib(n + 4) - (3 + n)
