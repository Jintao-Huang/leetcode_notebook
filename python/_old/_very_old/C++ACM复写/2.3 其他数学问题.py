# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 


def gcd(x: int, y: int) -> int:
    """最大公约数. O(1)"""
    while y > 0:
        x, y = y, x % y
    return x


def fib(n: int) -> int:
    """假设Fib(0) = 0, Fib(1) = 1. O(N)"""
    x, y = 0, 1
    while n > 0:
        x, y = y, x + y
        n -= 1
    return x


print(gcd(5, 4))
print(fib(10))
"""
1
0 1 1 2 3 5 8 13 21 34 55
"""


def lcm(x: int, y: int) -> int:
    """O(1)"""
    return x * y // gcd(x, y)


print(lcm(5, 4))  # 20


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


print(fast_pow(2, 100))
print(fast_pow(2, 100, 100000000000))
print(2 ** 100)
"""
1267650600228229401496703205376
96703205376
1267650600228229401496703205376
"""

from typing import List

Matrix = List[List[int]]


def matmul(m1: Matrix, m2: Matrix) -> Matrix:
    """Ot(Len(m1)Len(m2)Len(m2[0]))"""
    res = [[0] * len(m1) for _ in range(len(m2[0]))]
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            s = 0
            for k in range(len(m2)):
                s += m1[i][k] * m2[k][j]
            res[i][j] = s
    return res


print(matmul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
"""
[[7, 10], [15, 22]]
"""
