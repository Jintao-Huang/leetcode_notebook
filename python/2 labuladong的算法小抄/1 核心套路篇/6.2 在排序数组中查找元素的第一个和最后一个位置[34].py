# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List


def lower_bound(nums: List[int], target: int) -> int:
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] >= target:
            hi = mid
        else:
            lo = mid + 1
    return lo


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lo = lower_bound(nums, target)
        hi = lower_bound(nums, target + 1) - 1
        if lo < len(nums) and nums[lo] == target:
            return [lo, hi]
        else:
            return [-1, -1]


nums = [2, 2]
target = 3
print(Solution().searchRange(nums, target))
