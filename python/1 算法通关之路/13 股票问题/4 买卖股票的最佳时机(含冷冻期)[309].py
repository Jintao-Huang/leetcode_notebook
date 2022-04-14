# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # C: 卖出, 买入, 不变
        # dp_N^2[i][j]: 第j天, i=0不持有股票+下回合冻结, i=1不持有股票, i=2持有股票. 最大收益.
        dp = [[0] * len(prices) for _ in range(3)]
        dp[0][0] = 0
        dp[1][0] = 0
        dp[2][0] = -prices[0]
        for i in range(1, len(prices)):
            dp[0][i] = dp[2][i - 1] + prices[i]
            dp[1][i] = max(dp[0][i - 1], dp[1][i - 1])
            dp[2][i] = max(dp[2][i - 1], dp[1][i - 1] - prices[i])
        return max(dp[0][len(prices) - 1], dp[1][len(prices) - 1])


prices = [1, 2, 0, 1, 2]
print(Solution().maxProfit(prices))
