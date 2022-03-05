# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List


class Solution:
    """二分法. Ot(LogN) Os(1)"""

    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1


class Solution2:
    """二分法. Ot(LogN) Os(1). lower_bound框架"""

    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] >= target:
                hi = mid
            else:
                lo = mid + 1
        return lo if nums[lo] == target else -1


class Solution3:
    """二分法. Ot(LogN) Os(1). upper_bound框架"""

    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo + 1) // 2
            if nums[mid] <= target:
                lo = mid
            else:
                hi = mid - 1
        return lo if nums[lo] == target else -1


print(Solution().search([2, 2, 2, 2], 2))
print(Solution2().search([2, 2, 2, 2], 2))
print(Solution3().search([2, 2, 2, 2], 2))
