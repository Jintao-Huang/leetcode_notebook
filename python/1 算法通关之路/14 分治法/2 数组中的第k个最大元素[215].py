# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List
from heapq import nlargest


class Solution:
    """堆. Ot(K+NLogK+KLogK) Os(1). 平均复杂度. """

    def findKthLargest(self, nums: List[int], k: int) -> int:
        return nlargest(k, nums)[-1]


def partition(nums: List[int], lo: int, hi: int) -> int:
    """Ot(N) Os(1). [lo, hi]. 返回索引"""
    x = nums[lo]
    while lo < hi:
        while lo < hi and x <= nums[hi]:
            hi -= 1
        nums[lo] = nums[hi]
        while lo < hi and x >= nums[lo]:
            lo += 1
        nums[hi] = nums[lo]
    nums[lo] = x
    return lo


import random


class Solution2:
    """二分法. Ot(N) Os(1). 平均复杂度. """

    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            i = random.randint(lo, hi)
            nums[lo], nums[i] = nums[i], nums[lo]
            mid = partition(nums, lo, hi)
            if mid == k:
                return nums[mid]
            elif mid > k:
                hi = mid - 1
            else:
                lo = mid + 1
        return nums[lo]


nums = [3, 2, 1, 5, 6, 4]
k = 2
print(Solution().findKthLargest(nums, k))
print(Solution2().findKthLargest(nums, k))
