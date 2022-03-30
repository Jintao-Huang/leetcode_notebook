# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:
from typing import List


class Solution:
    """状态压缩"""

    def maxProfit(self, prices: List[int]) -> int:
        # C: 买, 卖, 不变
        # S: 是否含股票, 前i天, 交易j次最高收益.
        # dp[0][i][j]: dp[1][i-1][j-1]; dp[0][i-1][j]
        # dp[1][i][j]: dp[0][i-1][j]; dp[1][i-1][j]
        k = 2
        if len(prices) == 0:
            return 0
        dp = [[-int(1e8)] * (k + 1) for _ in range(2)]
        for i in range(len(prices)):
            for j in range(0, min(i, k) + 1):
                if i == 0 and j == 0:
                    dp[0][j] = 0
                    dp[1][j] = -prices[i]
                    continue
                if j == 0:
                    dp[0][j] = dp[0][j]  # 0
                    dp[1][j] = max(dp[1][j], -prices[i])
                    continue

                dp_0_j_copy = dp[0][j]
                dp[0][j] = max(dp[1][j - 1] + prices[i], dp[0][j])
                dp[1][j] = max(dp_0_j_copy - prices[i], dp[1][j])
        return max(dp[0])
