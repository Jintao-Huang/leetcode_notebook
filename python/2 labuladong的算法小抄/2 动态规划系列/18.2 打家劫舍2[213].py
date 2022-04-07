# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List


class Solution:
    """循环依赖关系, 动态规划难以处理. 此题特殊"""

    def _rob(self, nums: List[int], lo, hi) -> int:
        x, y = 0, nums[lo]  # 不抢, 抢
        for i in range(lo + 1, hi):
            x, y = max(x, y), x + nums[i]
        return max(x, y)

    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        return max(self._rob(nums, 0, len(nums) - 1),
                   self._rob(nums, 1, len(nums)))
