# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:
from typing import List


def k_c(W: List[int], V: List[int], C: int) -> int:
    # 其中W[i] >= 0
    INF = int(1e8)
    dp = [INF] * (C + 1)
    dp[0] = 0
    for i in range(C + 1):  # !
        for j in range(len(W)):
            if i - W[j] >= 0 and dp[i - W[j]] != INF:
                x = dp[i - W[j]] + V[j]
            else:
                x = INF
            dp[i] = min(dp[i], x)
    return dp[C]


class Solution:
    """动态规划. Ot(NM) Os(N). 其中N=amount, M=len(coins)"""

    # 完全按转义方程
    def coinChange(self, coins: List[int], amount: int) -> int:
        ans = k_c(coins, [1] * len(coins), amount)
        return ans if ans != int(1e8) else -1


print(Solution().coinChange([1, 2, 5], 11))
