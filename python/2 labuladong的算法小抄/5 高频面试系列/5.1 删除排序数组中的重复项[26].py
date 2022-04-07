# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        lo = 1
        for hi in range(1, len(nums)):
            if nums[hi] != nums[hi - 1]:
                nums[lo] = nums[hi]
                lo += 1
        return lo


nums = [1, 2, 3, 3, 4]
print(Solution().removeDuplicates(nums))
print(nums)
