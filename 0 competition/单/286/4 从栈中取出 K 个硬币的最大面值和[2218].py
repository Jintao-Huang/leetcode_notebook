# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List


class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        # 选择: len(piles[j])
        # dp[i][j]: 前i个堆, 共取j个. 最大收益
        # dp[i][j]; dp[i-1][k]
        dp = [[0] * (k + 1) for _ in range(len(piles) + 1)]
        for i in range(1, len(piles) + 1):
            for j in range(1, k + 1):
                s = 0
                for k2 in range(len(piles[i - 1]) + 1):
                    if k2 - 1 >= 0:  # 因果
                        s += piles[i - 1][k2 - 1]
                    if j - k2 < 0:  # 因果
                        break
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - k2] + s)

        return dp[len(piles)][k]


piles = [[1, 100, 3], [7, 8, 9]]
k = 2
print(Solution().maxValueOfCoins(piles, k))
piles = [[100], [100], [100], [100], [100], [100], [1, 1, 1, 1, 1, 1, 700]]
k = 7
print(Solution().maxValueOfCoins(piles, k))
