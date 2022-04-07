# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:
import math


class Solution:
    """数学"""

    def fib(self, n: int) -> int:
        """通项公式"""
        sqrt5 = math.sqrt(5)
        fibN = (((1 + sqrt5) / 2) ** n - ((1 - sqrt5) / 2) ** n) / sqrt5
        return round(fibN)


class Solution2:
    """动态规划-空间优化. Ot(N) Os(1). """

    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        x, y = 0, 1
        for _ in range(1, n):
            x, y = y, x + y
        return y


print(Solution2().fib(3))