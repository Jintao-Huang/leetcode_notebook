# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List


class Solution:
    """二分法. lower_bound2框架"""

    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] < nums[hi]:  # 永远不会等于, 因为mid!=hi.
                hi = mid
            else:
                lo = mid + 1
        return nums[lo]


# nums = [4, 5, 6, 0, 1, 2, 3]
nums = [4, 5, 6, 7, 0, 1, 2]
print(Solution().findMin(nums))
