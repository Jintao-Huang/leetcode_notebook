# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List


def k(W: List[int], C: int) -> int:
    # 状态压缩
    dp = [0] * (C + 1)
    dp[0] = 1
    for i in range(len(W)):
        for j in reversed(range(1, C + 1)):  # 从1开始, 因为不会有W[i] <= 0
            if j - W[i] >= 0:
                dp[j] += dp[j - W[i]]
    return dp[C]


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s = sum(nums)
        if abs(s) < abs(target) or (s + target) % 2 == 1:
            return 0
        C = (s + target) // 2
        #
        counter_0 = 0
        lo = 0
        for hi in range(len(nums)):
            x = nums[hi]
            if x == 0:
                counter_0 += 1
            else:
                nums[lo] = nums[hi]
                lo += 1
        for i in range(lo, len(nums)):
            nums.pop()
        #
        return k(nums, C) * 2 ** counter_0


nums = [1, 1, 1, 1, 1]
target = 3
print(Solution().findTargetSumWays(nums, target))
