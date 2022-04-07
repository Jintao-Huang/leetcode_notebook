# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:


from math import factorial


def comb(m: int, n: int) -> int:
    """m选n个"""
    return factorial(m) // factorial(n) // factorial(m - n)


def perm(m: int, n: int) -> int:
    return factorial(m) // factorial(m - n)
