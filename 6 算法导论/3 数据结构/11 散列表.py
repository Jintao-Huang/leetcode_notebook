# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List, Optional

"""11 散列表"""


# 直接寻址表
class DirectAddressTable:
    # p143. 利用数组进行散列
    # 条件: 没有相同key
    def __init__(self, lo: int, hi: int):
        # [lo..hi]
        n = hi - lo + 1
        self.lo = lo
        self.T = [None] * n  # type: List[Optional[int]]

    def direct_address_search(self, k: int) -> int:
        # k: idx
        k -= self.lo
        if self.T[k] is None:
            raise KeyError("empty key")
        else:
            return self.T[k]

    def direct_address_insert(self, k: int, x: int) -> None:
        k -= self.lo
        if self.T[k] is not None:
            raise KeyError("k already alloc")
        else:
            self.T[k] = x

    def direct_address_delete(self, k: int) -> None:
        k -= self.lo
        if self.T[k] is None:
            raise KeyError("empty key")
        else:
            self.T[k] = None


# if __name__ == '__main__':
#     dat = DirectAddressTable(1, 3)
#     # dat.direct_address_search(1)  # empty key
#     dat.direct_address_insert(1, 2)
#     print(dat.direct_address_search(1))
#     # dat.direct_address_insert(1, 2)  # 'k already alloc'
#     dat.direct_address_insert(2, 3)
#     dat.direct_address_insert(3, 4)
#     dat.direct_address_delete(2)
#     # dat.direct_address_delete(2)  # 'empty key'

from typing import Callable


# 散列表
class HashTable:
    # p144
    # 链接法
    def __init__(self, n: int, hash_func: Callable[[int], int]):
        self.T = [[] for _ in range(n)]
        self.hash_func = hash_func

    def chained_hash_insert(self, k: int, x: int) -> None:
        self.T[self.hash_func(k)].append((k, x))

    def chained_hash_search(self, k: int) -> int:
        ll = self.T[self.hash_func(k)]
        for kx, x in ll:
            if kx == k:
                return x
        raise KeyError("not found")

    def chained_hash_delete(self, k: int) -> None:
        ll = self.T[self.hash_func(k)]
        for i in range(len(ll)):
            kx = ll[i][0]
            if kx == k:
                ll.pop(i)
                return
        raise KeyError("not found")


# if __name__ == '__main__':
#     def gen_hf(n :int) -> Callable[[int], int]:
#         def hf(k: int):
#             return k % n
#         return hf
#     ht = HashTable(3, gen_hf(3))
#     # print(ht.chained_hash_search(1))  # 'not found'
#     ht.chained_hash_insert(1, 3)
#     ht.chained_hash_insert(4, 2)
#     print(ht.chained_hash_search(1))
#     print(ht.chained_hash_search(4))
#     # print(ht.chained_hash_search(2))  # 'not found'
#     ht.chained_hash_delete(1)
#     # print(ht.chained_hash_search(1))  # 'not found'
#     print(ht.chained_hash_search(4))
#     # ht.chained_hash_delete(1)  # 'not found'

# 散列函数
"""
1. p147. 启发式方法: 除法散列, 乘法散列. 全域散列: 随机技术
    字符串key, 可以使用*基数转为整数, 再%
"""


# 常见素数
# 11
# 101
# 1009
# 10007
# int(1e5)+3
# int(1e6)+3
#
# int(1e7)+19
# int(1e8)+7
# int(1e9)+7
#
# int(1e16)+61
# int(1e17)+3
# int(1e18)+3
def divide_hashing(m: int) -> Callable[[int], int]:
    # p148
    # m要为素数
    def hash_func(k: int):
        return k % m

    return hash_func


import math


def multiply_hashing(m: int, A: float = None) -> Callable[[int], int]:
    # p148
    # A: float in (0..1).
    if A is None:
        A = (math.sqrt(5) - 1) / 2

    def hash_fun(k: int):
        return int(m * (k * A % 1))  # 对m的选择不关键, e.g: m = 2^p

    return hash_fun


# if __name__ == '__main__':
#     print(divide_hashing(701)(2000))
#     k = 123456
#     p = 14
#     m = 2 ** p
#     w = 32  # 字长
#     A = 2654435769 / 2 ** 32
#     print(multiply_hashing(m, A)(k))
#     print(multiply_hashing(m)(k))

from random import randint


def universal_hashing(p: int, m: int, a: int = None, b: int = None) -> Callable[[int], int]:
    # p150
    if a is None:
        a = randint(1, p - 1)
    if b is None:
        b = randint(0, p - 1)

    def hash_func(k: int):
        return ((a * k + b) % p) % m

    return hash_func


# if __name__ == '__main__':
#     print(universal_hashing(17, 6, 3, 4)(8))

"""
1. p151. 开放寻址法. 无指针, 节省空间, 更多槽, 减少冲突.
"""


class OpenAddress:
    # p152
    def __init__(self, m: int, h: Callable[[int, int], int]):
        # h: get探查序列. <h(k,0), h(k,1)...>
        self.T = [None] * m  # type: List[Optional[int]]
        self.h = h

    def hash_insert(self, k: int) -> int:
        i = 0
        while True:
            j = self.h(k, i)
            if self.T[j] is None:
                self.T[j] = k
                return j
            else:
                i += 1
            if i == len(self.T):
                raise OverflowError("hash table overflow")

    def hash_search(self, k: int) -> int:
        i = 0
        while True:
            j = self.h(k, i)
            if self.T[j] == k:
                return j
            i += 1
            if self.T[j] is None or i == len(self.T):
                raise KeyError("not found")

    # note: 删除不能用None来标识为空. 只能通过Deleted常量标识.
    # 然后hash_insert()将这样的槽作为空槽. 无需对hash_search()进行修改.
    # 开放寻址法更适用于: 只插入不删除的应用场景. 例如: const mapper. 否则: 用链接法


# 线性探查, 二次探查, 双重探查

def linear_probing(h: Callable[[int], int], m: int) -> Callable[[int, int], int]:
    # p153
    # 一次集群
    def hash_func2(k: int, i: int):
        return (h(k) + i) % m

    return hash_func2


# if __name__ == '__main__':
#     m = 4
#     h = universal_hashing(7, m)
#     h2 = linear_probing(h, m)
#     oa = OpenAddress(m, h2)
#     oa.hash_insert(0)
#     oa.hash_insert(7)
#     oa.hash_insert(14)
#     oa.hash_insert(21)
#     oa.hash_insert(21)  # hash table overflow
#     # print(oa.hash_search(8))  # not found
#     print(oa.hash_search(0))
#     print(oa.hash_search(7))
#     print(oa.hash_search(14))
#     print(oa.hash_search(21))


def quadratic_probing(h: Callable[[int], int], m: int, c1: int, c2: int) \
        -> Callable[[int, int], int]:
    # p153
    # 二次集群
    def hash_func2(k: int, i: int):
        return (h(k) + c1 * i + c2 * i * i) % m

    return hash_func2


def double_hashing(h: Callable[[int], int], h2: Callable[[int], int], m: int) \
        -> Callable[[int, int], int]:
    # p153
    def hash_func2(k: int, i: int):
        return (h(k) + i * h2(k)) % m

    return hash_func2

# if __name__ == '__main__':
#     m = 701
#     h1 = divide_hashing(m)
#     h2 = lambda k: 1 + (k % (m - 1))
#     k = 123456
#     print(double_hashing(h1, h2, m)(k, 0))
#     print(double_hashing(h1, h2, m)(k, 1))


# 1. p156. 完全散列. 略. 下面是e.g.

# if __name__ == '__main__':
#     # 一级散列
#     h = universal_hashing(101, 9, 3, 42)
#     print(h(75))
#     # 二级散列
#     h2 = universal_hashing(101, 9, 10, 18)
#     print(h2(75))
