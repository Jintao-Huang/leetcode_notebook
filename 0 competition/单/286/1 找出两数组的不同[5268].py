# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List


class Solution:
    """set diff"""
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        ans = nums1 - nums2
        ans2 = nums2 - nums1
        return [list(ans), list(ans2)]


nums1 = [1, 2, 3]
nums2 = [2, 4, 6]
print(Solution().findDifference(nums1, nums2))

nums1 = [1, 2, 3, 3]
nums2 = [1, 1, 2, 2]
print(Solution().findDifference(nums1, nums2))
