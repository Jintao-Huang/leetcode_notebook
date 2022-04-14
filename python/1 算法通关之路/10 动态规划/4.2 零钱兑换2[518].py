# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List


class Solution2:
    """动态规划. Ot(NM) Os(NM). 其中N=amount, M=len(coins)"""

    def change(self, amount: int, coins: List[int]) -> int:
        # 选择: 取c: dp_N^2[i][j-c], 不取c: dp_N^2[i-1][j]. 选择与dp维度, 存在关联.
        # dp_N^2[i][j]. 由前i种coins, 凑成j的组合数.
        # base: dp_N^2[0][j] = 1
        # 转移: dp_N^2[i][j] = dp_N^2[i][j - c] + dp_N^2[i - 1][j]
        dp = [[0] * (amount + 1) for _ in range(len(coins))]
        for i in range(len(coins)):
            c = coins[i]
            dp[i][0] = 1
            for j in range(1, amount + 1):
                if j - c >= 0:
                    dp[i][j] += dp[i][j - c]
                if i >= 1:
                    dp[i][j] += dp[i - 1][j]
        return dp[-1][-1]


class Solution:
    """动态规划-空间优化. Ot(NM) Os(N). 其中N=amount"""

    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for c in coins:
            for i in range(c, amount + 1):
                dp[i] += dp[i - c]
        return dp[-1]


amount = 5
coins = [1, 2, 5]
print(Solution().change(amount, coins))
print(Solution2().change(amount, coins))
