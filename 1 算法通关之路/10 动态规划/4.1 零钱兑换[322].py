# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List


class Solution:
    """动态规划. Ot(NM) Os(N). 其中N=amount, M=len(coins)"""

    def coinChange(self, coins: List[int], amount: int) -> int:
        # 选择: coins中选
        # dp[i] 凑成i元所需的最少硬币个数.
        # base: dp[0]=0
        # 转移: dp[i]=min(dp[i-ci]) 任意ci属于coins
        dp = [int(1e8)] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                if i >= c:
                    dp[i] = min(dp[i - c] + 1, dp[i])

        return -1 if dp[-1] == int(1e8) else dp[-1]


coins = [1, 2, 5]
amount = 11
print(Solution().coinChange(coins, amount))
