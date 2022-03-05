# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List


class Solution:
    """二分法. Ot(NLogM) Os(1): N=len(nums), M=sum(nums).
    lower_bound2框架"""

    def test(self, nums: List[int], m: int, k: int) -> bool:
        t = k
        m -= 1
        for i in range(len(nums)):
            if t < nums[i]:
                t = k
                m -= 1
            t -= nums[i]
            if m < 0:
                return False
        return True

    def splitArray(self, nums: List[int], m: int) -> int:
        lo, hi = max(nums), sum(nums)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if self.test(nums, m, mid):
                hi = mid
            else:
                lo = mid + 1
        return lo


nums = [7, 2, 5, 10, 8]
m = 2
print(Solution().splitArray(nums, m))
