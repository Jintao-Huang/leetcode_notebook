# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

"""
1. 动态规划的函数式有一个 方向性
  e.g. 从上往下 从左往右


"""


class Solution509:
    """斐波那契数. 见递归"""


class Solution322:
    """零钱兑换. 见贪心"""


class Solution62:
    """不同路径"""

    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                dp[i][j] = (dp[i - 1][j] if i - 1 >= 0 else 0) + \
                           (dp[i][j - 1] if j - 1 >= 0 else 0)
        return dp[-1][-1]


m = 3
n = 2
print(Solution62().uniquePaths(m, n))

from typing import List


class Solution121:
    """买卖股票的最佳时机"""

    def maxProfit(self, prices: List[int]) -> int:
        """动态规划. Ot(N)"""
        max_p = prices[-1]
        res = 0
        for i in reversed(range(len(prices) - 1)):
            max_p = max(max_p, prices[i])
            res = max(max_p - prices[i], res)

        return res

    def maxProfit2(self, prices: List[int]) -> int:
        min_p = prices[0]
        res = 0
        for i in range(1, len(prices)):
            min_p = min(prices[i], min_p)
            res = max(prices[i] - min_p, res)
        return res


prices = [7, 6, 4, 3, 1]
print(Solution121().maxProfit(prices))


class Solution70:
    """爬楼梯"""

    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = [-1] * n
        dp[0], dp[1] = 1, 2
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n - 1]

    def climbStairs2(self, n: int) -> int:
        x, y = 1, 2
        for i in range(n - 1):
            x, y = y, x + y
        return x


print(Solution70().climbStairs(10))
print(Solution70().climbStairs2(10))

import math


class Solution279:
    """完全平方树"""

    def __init__(self):
        self.v: List[int] = [(i + 1) ** 2 for i in range(100)]

    def numSquares(self, n: int) -> int:
        """动态规划. Ot(N * sqrt(N))"""
        length = int(math.sqrt(n))
        INF = int(1e9)
        v = self.v[:length]
        dp = [INF] * n
        for i in range(len(v)):
            for j in range(v[i] - 1, n):
                k = j - v[i]
                dp[j] = min(dp[j], (dp[k] if k >= 0 else 0) + 1)
        return dp[-1]


n = 12
print(Solution279().numSquares(n))
