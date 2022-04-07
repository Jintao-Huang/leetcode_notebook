# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List


class Solution:
    """滑动窗口"""

    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        lo, hi = 0, 0
        ans = []
        for hi in range(len(nums)):
            if nums[hi] == key:
                lo = max(lo, hi - k)
                while lo - hi <= k and lo < len(nums):
                    if hi - lo <= k:
                        ans.append(lo)
                    lo += 1
        return ans


nums = [3, 4, 9, 1, 3, 9, 5]
key = 9
k = 1
print(Solution().findKDistantIndices(nums, key, k))
nums = [2, 2, 2, 2, 2]
key = 2
k = 2
print(Solution().findKDistantIndices(nums, key, k))
nums = [1, 1000, 1, 1000]
key = 1
k = 1
print(Solution().findKDistantIndices(nums, key, k))
