# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 


class Solution:
    """超时. 动态规划."""

    def superEggDrop(self, k: int, n: int) -> int:
        # dp[i][j]: i+1个蛋, 楼层数为j+1. 的最小操作次数
        # dp[i][j]; dp[i-1][k-1], dp[i][j-k]
        # 选择: 选一层楼投
        dp = [[0] * (n + 1) for _ in range(k)]
        for i in range(k):
            for j in range(n + 1):
                if i == 0:
                    dp[i][j] = j
                    continue
                if j == 0:
                    dp[i][j] = 0
                    continue
                dp[i][j] = int(1e8)
                for ii in range(1, j + 1):  # ii层扔
                    dp[i][j] = min(dp[i][j], max(
                        dp[i - 1][ii - 1], dp[i][j - ii]  # 可能j也不碎
                    ) + 1)
        print(dp)
        return dp[k - 1][n]


class Solution2:
    """超时. 动态规划+二分"""

    def superEggDrop(self, k: int, n: int) -> int:
        # dp[i][j]: i+1个蛋, 楼层数为j+1. 的最小操作次数
        # dp[i][j]; dp[i-1][k-1], dp[i][j-k]
        dp = [[0] * (n + 1) for _ in range(k)]
        for i in range(k):
            for j in range(n + 1):
                if i == 0:
                    dp[i][j] = j
                    continue
                if j == 0:
                    dp[i][j] = 0
                    continue
                dp[i][j] = int(1e8)
                # 二分
                lo, hi = 1, j
                while lo < hi:
                    mid = lo + (hi - lo) // 2
                    if dp[i - 1][mid - 1] >= dp[i][j - mid]:  # 第一个
                        hi = mid
                    else:
                        lo = mid + 1
                dp[i][j] = max(dp[i - 1][lo - 1], dp[i][j - lo]) + 1

        return dp[k - 1][n]


class Solution3:
    """二分法+memo"""

    def __init__(self):
        self.memo = {}

    def _dp(self, i: int, j: int) -> int:
        if (i, j) in self.memo:
            return self.memo[(i, j)]
        if i == 0:
            return j
        if j == 0:
            return 0
        # 二分
        lo, hi = 1, j
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if self._dp(i - 1, mid - 1) >= self._dp(i, j - mid):  # 第一个
                hi = mid
            else:
                lo = mid + 1
        self.memo[(i, j)] = max(self._dp(i - 1, lo - 1), self._dp(i, j - lo)) + 1

        return self.memo[(i, j)]

    def superEggDrop(self, k: int, n: int) -> int:

        return self._dp(k - 1, n)


import sys

sys.setrecursionlimit(10000)

print(Solution2().superEggDrop(100, 8191))
print(Solution3().superEggDrop(100, 8191))
