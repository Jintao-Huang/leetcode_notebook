# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List


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


class Solution:
    """用记忆. Ot(N) Os(1)"""

    def __init__(self):
        prime = get_prime_nums(100)
        self.helper = []
        self.fac = {0: 1}
        self.mod = int(1e9 + 7)
        i = 0
        for x in range(101):
            if i < len(prime) and x == prime[i]:
                i += 1
            self.helper.append(i)

    def _factorial(self, i: int) -> int:
        mod = self.mod
        if i in self.fac:
            return self.fac[i]
        self.fac[i] = self._factorial(i - 1) * i % mod

        return self.fac[i]

    def numPrimeArrangements(self, n: int) -> int:
        x = self.helper[n]
        return self._factorial(x) * self._factorial(n - x) % self.mod


from math import factorial


class Solution2:
    """用math模块. Ot(N) Os(1)"""

    def __init__(self):
        prime = get_prime_nums(100)
        self.helper = []
        self.mod = int(1e9 + 7)
        i = 0
        for x in range(101):
            if i < len(prime) and x == prime[i]:
                i += 1
            self.helper.append(i)

    def numPrimeArrangements(self, n: int) -> int:
        x = self.helper[n]
        return factorial(x) * factorial(n - x) % self.mod


print(Solution().numPrimeArrangements(100))
print(Solution2().numPrimeArrangements(100))
