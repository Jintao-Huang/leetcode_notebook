# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 
from typing import List


class Solution:
    """二分. 一线划分"""
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        m = len(nums1)
        n = len(nums2)  # m <= n
        lo, hi = 0, m  # 在线右
        while lo <= hi:
            # 想象mid1, mid2是索引左边的两条线
            mid1 = lo + (hi - lo) // 2
            mid2 = (m + n) // 2 - mid1  # 后面多一个
            n1 = nums1[mid1 - 1] if mid1 >= 1 else -int(1e8)
            n2 = nums1[mid1] if mid1 < m else int(1e8)
            n3 = nums2[mid2 - 1] if mid2 >= 1 else -int(1e8)
            n4 = nums2[mid2] if mid2 < n else int(1e8)
            if lo == hi:
                ans1 = max(n1, n3)
                ans2 = min(n2, n4)
                return (ans1 + ans2) / 2 if (m + n) % 2 == 0 else ans2
            if n2 >= n3:
                hi = mid1
            else:
                lo = mid1 + 1


nums1 = [1, 3]
nums2 = [2]
print(Solution().findMedianSortedArrays(nums1, nums2))
nums1 = []
nums2 = [1]
print(Solution().findMedianSortedArrays(nums1, nums2))
nums1 = []
nums2 = [1, 2, 3, 4]
print(Solution().findMedianSortedArrays(nums1, nums2))
nums1 = [1, 3]
nums2 = [2, 7]
print(Solution().findMedianSortedArrays(nums1, nums2))
