# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:

from math import factorial


def comb(m: int, n: int) -> int:
    """m选n个"""
    return factorial(m) // factorial(n) // factorial(m - n)


class Solution:
    """数学. Ot(N) Os(1)"""

    def uniquePaths(self, m: int, n: int) -> int:
        return comb(m + n - 2, n - 1)


class Solution2:
    """动态规划. Ot(N^2) Os(N^2)"""

    def uniquePaths(self, m: int, n: int) -> int:
        # dp[i, j]. 以i,j结尾的路径数
        # base: dp[i][j] = 1. if i==0 or j==0
        # 转移: dp[i][j]=dp[i-1][j]+dp[i][j-1]
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]


print(Solution().uniquePaths(3, 7))
print(Solution2().uniquePaths(3, 7))
