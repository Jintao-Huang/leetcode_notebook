# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:
from typing import List, Dict

import math


def is_prime_num(x: int) -> bool:
    """Ot(Sqrt(N))"""
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    else:
        return True


print(is_prime_num(11))
print(is_prime_num(25))
"""
True
False
"""


def get_prime_nums(n: int) -> List[int]:
    """Ot(N^2). 一般n只需要sqrt(x)即可. 不含n"""
    res = []
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False
    for i in range(2, n):
        if not is_prime[i]:
            continue
        else:
            res.append(i)
            for j in range(i * i, n, i):
                is_prime[j] = False
    return res


r = get_prime_nums(97)
for x in r:
    if not is_prime_num(x):
        print(x)
print(r)  # 不含97
"""
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89]

"""


def get_prime_factor(x: int) -> Dict[int, int]:
    """含每个质因数的次数. Ot(N)"""
    res = {}
    prime_list = get_prime_nums(int(math.sqrt(x)) + 1)
    for p in prime_list:
        while x % p == 0:
            x /= p
            if p in res:
                res[p] += 1
            else:
                res[p] = 1
        if p > x:
            break
    if x > 1:
        res[x] = 1
    return res


print(get_prime_factor(100011))
print(get_prime_factor(53))
print(get_prime_factor(64))
"""
{3: 1, 17: 1, 37: 1, 53: 1}
{53: 1}
{2: 6}
"""


def get_factor(x: int) -> List[int]:
    """不含每个因数的次数. Ot(Sqrt(N))"""
    res = []
    for i in range(1, int(math.sqrt(x)) + 1):
        if x % i == 0:
            j = x // i
            res += [i, j] if i != j else [i]
    return res


print(get_factor(53))
print(get_factor(64))
"""
[1, 53]
[1, 64, 2, 32, 4, 16, 8]
"""


def get_n_factor(x: int) -> int:
    """Ot(N)"""
    pf = get_prime_factor(x)
    res = 1
    for n in pf.values():
        res *= n + 1
    return res


def get_n_factor2(x: int) -> int:
    """Ot(Sqrt(N))"""
    return len(get_factor(x))


print(get_n_factor(53))
print(get_n_factor(64))
print(get_n_factor2(53))
print(get_n_factor2(64))
"""
2
7
2
7
"""
