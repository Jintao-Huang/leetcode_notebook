# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:

from typing import List, Dict, Tuple, Set


class _Solution:
    """排序+双指针. 错误. """

    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n1, n2, n3, n4 = len(nums1), len(nums2), len(nums3), len(nums4)
        nums3.sort()
        nums4.sort()
        ans = 0
        for i in range(n1):
            for j in range(n2):
                lo, hi = 0, n4 - 1
                while lo < n3 and hi >= 0:
                    x = nums1[i] + nums2[j] + nums3[lo] + nums4[hi]
                    if x == 0:
                        ans += 1
                        lo += 1
                        hi -= 1
                    elif x < 0:
                        lo += 1
                    else:
                        hi -= 1
        return ans


class Solution:
    """哈希表. Ot(N^2) Os(N^2)"""

    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n1, n2, n3, n4 = len(nums1), len(nums2), len(nums3), len(nums4)
        d = {}  # type: Dict[int, int]  # 值, 个数
        ans = 0
        for i in range(n1):
            for j in range(n2):
                x = nums1[i] + nums2[j]
                if x not in d:
                    d[x] = 0
                d[x] += 1
        for i in range(n3):
            for j in range(n4):
                x = nums3[i] + nums4[j]
                if -x in d:
                    ans += d[-x]

        return ans

nums1 = [0, 1, -1]
nums2 = [-1, 1, 0]
nums3 = [0, 0, 1]
nums4 = [-1, 1, 1]
print(_Solution().fourSumCount(nums1, nums2, nums3, nums4))  # 17
print(Solution().fourSumCount(nums1, nums2, nums3, nums4))  # 17


