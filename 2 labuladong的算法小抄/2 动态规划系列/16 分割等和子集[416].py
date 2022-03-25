# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:

from typing import List


def k(W: List[int], V: List[int], C: int) -> int:
    # 状态压缩
    dp = [0] * (C + 1)
    for i in range(len(W)):
        for j in reversed(range(1, C + 1)):
            if j - W[i] >= 0:
                dp[j] = max(dp[j], dp[j - W[i]] + V[i])  # min
    return dp[C]


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 == 1:
            return False
        s //= 2
        return True if k(nums, nums, s) == s else False


# 装满
def k_full(W: List[int], V: List[int], C: int) -> int:
    N_INF = int(-1e8)  # INF
    dp = [N_INF] * (C + 1)
    dp[0] = 0
    for i in range(len(W)):
        for j in reversed(range(C + 1)):
            if j - W[i] >= 0 and dp[j - W[i]] != N_INF:
                dp[j] = max(dp[j], dp[j - W[i]] + V[i])  # min
    return dp[C]


class Solution2:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 == 1:
            return False
        s //= 2
        return k_full(nums, nums, s) != int(-1e8)


print(Solution().canPartition(nums=[1, 2, 5]))
print(Solution2().canPartition(nums=[1, 2, 5]))
