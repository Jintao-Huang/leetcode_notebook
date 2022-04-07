# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List


class Solution:
    """动态规划. Ot(N) Os(1)"""
    def _rob(self, nums: List[int], lo: int, hi: int) -> int:
        x, y = nums[lo], max(nums[lo], nums[lo + 1])
        for i in range(lo + 2, hi):
            x, y = y, max(x + nums[i], y)
        return y

    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        return max(self._rob(nums, 0, len(nums) - 1),
                   self._rob(nums, 1, len(nums)))
