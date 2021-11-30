# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

"""
https://leetcode-cn.com/problems/coin-change/
322. 零钱兑换
- 中等
- 推荐
- 模板: 动态规划
=
- 动态规划
- 完全背包问题: 最少, 需装满(=amount)
  凑成[总金额]所需的最少的[硬币个数]
  v: 1; w: coins; C: amount
"""
from typing import List, Tuple
from functools import lru_cache


class Solution:
    """dfs"""

    def coinChange(self, coins: List[int], amount: int) -> int:
        INT_MAX = int(1e9)

        @lru_cache(amount + 3)  # 有少量空余
        def _dp(i: int) -> int:
            nonlocal INT_MAX
            # 1. base
            if i == 0:
                return 0
            # 2. dp初始化
            ans = INT_MAX
            # 3. 搜索
            for c in coins:
                if i - c <= -1:
                    continue
                ans = min(ans, _dp(i - c) + 1)
            return ans

        # 4.
        ans = _dp(amount)
        return -1 if ans == INT_MAX else ans


coins = [186, 419, 83, 408]
amount = 6249
print(Solution().coinChange(coins, amount))  # 3


class Solution2:
    """动态规划"""

    def coinChange(self, coins: List[int], amount: int) -> int:
        # 1. 2.
        INT_MAX = 0x7ff_ffff
        dp = [INT_MAX] * (amount + 1)  # [0 - amount]
        dp[0] = 0  # base
        #
        for i in range(1, amount + 1):
            # 3. 搜索
            for c in coins:
                if i - c <= -1:
                    continue
                dp[i] = min(dp[i], dp[i - c] + 1)
        # 4.
        ans = dp[-1]
        return -1 if ans == INT_MAX else ans


coins = [186, 419, 83, 408]
amount = 6249
print(Solution2().coinChange(coins, amount))  # 3
