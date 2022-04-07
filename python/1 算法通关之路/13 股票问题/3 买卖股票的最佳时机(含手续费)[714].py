# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List


class Solution:
    """DP"""

    def maxProfit(self, prices: List[int], fee: int) -> int:
        # C: 卖出, 买入, 不变
        # dp[i][j]: 第j天, i=0不持有股票, i=1持有股票的最大收益.
        dp = [[0] * len(prices) for _ in range(2)]
        dp[0][0] = 0
        dp[1][0] = -prices[0]
        for i in range(1, len(prices)):
            dp[0][i] = max(dp[0][i - 1], dp[1][i - 1] + prices[i] - fee)
            dp[1][i] = max(dp[1][i - 1], dp[0][i - 1] - prices[i])
        return dp[0][len(prices) - 1]


prices = [1, 3, 2, 8, 4, 9]
print(Solution().maxProfit(prices, 2))


class Solution2:
    """状态压缩"""

    def maxProfit(self, prices: List[int], fee: int) -> int:
        # C: 卖出, 买入.
        # dp[i][j]: 第j天, i=0不持有股票, i=1持有股票的最大收益.
        dp0 = 0
        dp1 = -prices[0]
        for i in range(1, len(prices)):
            dp0_copy = dp0
            dp0 = max(dp0, dp1 + prices[i] - fee)
            dp1 = max(dp1, dp0_copy - prices[i])
        return dp0


print(Solution2().maxProfit(prices, 2))


class Solution3:
    """贪心"""

    def maxProfit(self, prices: List[int], fee: int) -> int:

        min_ = prices[0] + fee  # 卖出fee, 变为买入fee
        ans = 0
        for i in range(1, len(prices)):
            x = prices[i]
            if x > min_:
                ans += x - min_
                min_ = x
            elif x + fee < min_:
                min_ = x + fee
        return ans


prices = [1, 3, 7, 5, 10, 3]
print(Solution3().maxProfit(prices, 3))
