# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List


class Solution:
    """贪心"""

    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        for i in range(1, len(prices)):
            ans += max(0, prices[i] - prices[i - 1])
        return ans

    def maxProfit2(self, prices: List[int]) -> int:
        ans = 0
        min_ = prices[0]
        for i in range(1, len(prices)):
            x = prices[i]
            if x > min_:
                ans += x - min_
            min_ = x
        return ans


print(Solution().maxProfit(prices=[7, 1, 5, 3, 6, 4]))
print(Solution().maxProfit2(prices=[7, 1, 5, 3, 6, 4]))


class Solution2:
    """DP"""

    def maxProfit(self, prices: List[int]) -> int:
        # C: 卖出, 买入.
        # dp_N^2[i][j]: 第j天, i=0不持有股票, i=1持有股票的最大收益.
        dp = [[0] * len(prices) for _ in range(2)]
        dp[0][0] = 0
        dp[1][0] = -prices[0]
        for i in range(1, len(prices)):
            dp[0][i] = max(dp[0][i - 1], dp[1][i - 1] + prices[i])
            dp[1][i] = max(dp[1][i - 1], dp[0][i - 1] - prices[i])
        return dp[0][len(prices) - 1]


print(Solution2().maxProfit(prices=[7, 1, 5, 3, 6, 4]))
