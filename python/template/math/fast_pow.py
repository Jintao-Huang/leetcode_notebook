# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:

# 372
"""a^[a,b,c]=a^c*(a^10)^[a,b]"""


#
def fast_pow(x: int, y: int, mod: int = None) -> int:
    """Ot(Log(Y))"""
    res = 1
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
    print(fast_pow(2, 100))
    print(2 ** 100)
    print(fast_pow(2, 100, 100000000000))
    print(2 ** 100 % 100000000000)

    """Out
    1267650600228229401496703205376
    1267650600228229401496703205376
    96703205376
    96703205376
    """
