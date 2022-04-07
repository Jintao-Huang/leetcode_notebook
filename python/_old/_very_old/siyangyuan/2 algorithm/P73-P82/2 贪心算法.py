# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List


class Solution322:
    """零钱兑换"""

    def coinChange(self, coins: List[int], amount: int) -> int:
        """不行. Ot(^)"""
        res = 0
        coins.sort()  # 小 -> 大
        c = []

        def _coinChange(j: int) -> bool:
            nonlocal res, amount
            if amount == 0:
                return True
            for i in reversed(range(j)):
                if amount >= coins[i]:
                    res += 1
                    c.append(coins[i])
                    amount -= coins[i]
                    if _coinChange(i + 1):
                        return True
                    res -= 1
                    amount += coins[i]
                    c.pop()
            return False

        return res if _coinChange(len(coins)) else -1

    def coinChange2(self, coins: List[int], amount: int) -> int:
        """动态规划. Ot(Len(C)A)"""
        if amount == 0:
            return 0
        INF = 0x7fffffff // 10
        dp = [INF] * amount
        for i in range(len(coins)):
            for j in range(coins[i] - 1, amount):
                k = j - coins[i]
                dp[j] = min(dp[j], (dp[k] if k >= 0 else 0) + 1)
        return dp[amount - 1] if dp[amount - 1] != INF else -1
    # coins = [1, 2, 5]


# amount = 11
# print(Solution322().coinChange(coins, amount))
coins = [186, 419, 83, 408]
amount = 6249
# print(Solution322().coinChange(coins, amount))  # 20
print(Solution322().coinChange2(coins, amount))  # 20


class Solution1217:
    """玩筹码"""

    def minCostToMoveChips(self, position: List[int]) -> int:
        ji = 0
        for p in position:
            if p % 2 == 1:
                ji += 1
        ou = len(position) - ji
        return min(ji, ou)


chips = [2, 2, 2, 3, 3]
print(Solution1217().minCostToMoveChips(chips))

"""
1. 从头往后看
2. 从后往前看
"""


class Solution55:
    def canJump(self, nums: List[int]) -> bool:
        """超时. """
        dp = [False] * len(nums)
        dp[-1] = True
        for i in reversed(range(len(nums) - 1)):
            for j in range(nums[i] + 1):
                if i + j < len(nums) and dp[i + j] is True:
                    dp[i] = True
                    break
        return dp[0]

    def canJump2(self, nums: List[int]) -> bool:
        """贪心. Ot(N) Os(1)"""
        idx = len(nums) - 1
        for i in reversed(range(len(nums) - 1)):
            if i + nums[i] >= idx:
                idx = i
        return True if idx == 0 else False

    def canJump3(self, nums: List[int]) -> bool:
        """贪心. Ot(N) Os(1)"""
        idx = nums[0]
        for i in range(1, len(nums) - 1):
            if i <= idx <= i + nums[i]:
                idx = i + nums[i]
        return True if idx >= (len(nums) - 1) else False


nums = [2, 3, 1, 1, 4]
print(Solution55().canJump(nums))
print(Solution55().canJump2(nums))
print(Solution55().canJump3(nums))
