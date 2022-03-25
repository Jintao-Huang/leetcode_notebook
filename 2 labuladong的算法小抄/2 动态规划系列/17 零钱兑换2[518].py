# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List


def k_c(W: List[int], C: int) -> int:
    dp = [0] * (C + 1)
    dp[0] = 1
    for i in range(len(W)):
        for j in range(1, C + 1):  # !
            if j - W[i] >= 0:
                dp[j] += dp[j - W[i]]
    return dp[C]


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        return k_c(coins, amount)


print(Solution().change(5, [1, 2, 5]))
