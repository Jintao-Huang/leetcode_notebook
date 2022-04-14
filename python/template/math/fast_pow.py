# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:

# 372
"""a^[a,b,c]=a^c*(a^10)^[a,b]"""
import math


#
def fast_pow(x: float, y: int, mod: int = None) -> float:
    """Ot(Log(Y))."""
    res = 1
    if y < 0:
        y = -y
        x = 1 / x
    #
    while y > 0:
        if y % 2 == 1:
            res *= x
        x *= x
        y //= 2
        if mod:
            res %= mod
            x %= mod
    return res


if __name__ == '__main__':
    # test
    # print(fast_pow(2, 100))
    print(fast_pow(2, -4))
    print(2 ** 100)
    print(fast_pow(2, 100, 100000000000))
    print(2 ** 100 % 100000000000)

    """Out
    1267650600228229401496703205376
    1267650600228229401496703205376
    96703205376
    96703205376
    """
