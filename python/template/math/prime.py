# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

import math
from typing import List, Dict
# import numba
#
# @numba.njit
def is_prime_num(x: int) -> bool:
    """Ot(sqrt(N)) Os(1)"""
    if x < 2:
        return False
    #
    for i in range(2, int(math.sqrt(x)) + 1):  # [2...sqrt(x)]
        if x % i == 0:
            return False
    return True


def get_prime_nums(n: int) -> List[bool]:
    """Ot(NLogN) Os(N). 求[0...n)内的质数"""
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False
    #
    for i in range(2, n):
        if not is_prime[i]:
            continue
        #
        for j in range(i * i, n, i):
            is_prime[j] = False
    return is_prime


def to_prime_factor(x: int) -> Dict[int, int]:
    """分解质因素. Ot(N)"""
    res = {}
    prime_list = get_prime_nums(int(math.sqrt(x)) + 1)
    for p in prime_list:
        #
        while x % p == 0:
            x /= p
            if p not in res:
                res[p] = 0
            res[p] += 1
        #
        if p > x:
            break
    if x > 1:
        res[x] = 1
    return res


def factor_num(x: int) -> int:
    """求因数个数"""
    res = 0
    for i in range(1, int(math.sqrt(x)) + 1):
        if x % i == 0:
            j = x // i
            res += (2 if i != j else 1)
    return res
