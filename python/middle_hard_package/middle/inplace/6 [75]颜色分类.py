# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:

from typing import List


def partition(nums, lo, hi, p):
    x = nums[lo]
    while lo < hi:
        while lo < hi and nums[hi] >= p:
            hi -= 1
        nums[lo] = nums[hi]
        while lo < hi and nums[lo] < p:
            lo += 1
        nums[hi] = nums[lo]
    nums[lo] = x
    return lo


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # 两次partition
        lo, hi = 0, len(nums) - 1
        # find first 1,2
        while lo < hi and nums[lo] == 0:
            lo += 1
        lo = partition(nums, lo, hi, 1)
        while lo < hi and nums[lo] == 1:
            lo += 1
        partition(nums, lo, hi, 2)


# Solution().sortColors([2, 0, 2, 1, 1, 0])
Solution().sortColors([0])


class Solution2:
    def sortColors(self, nums: List[int]) -> None:

        lo, hi = 0, len(nums) - 1
        # ..lo-1: 0, hi+1..: 1
        i = 0
        while i <= hi:
            if nums[i] == 2:
                nums[i], nums[hi] = nums[hi], nums[i]
                hi -= 1
            elif nums[i] == 0:
                nums[i], nums[lo] = nums[lo], nums[i]
                lo += 1
                # nums[i] 只会是1, 若是0, 则一定在lo下面.
                i += 1
            else:
                i += 1
