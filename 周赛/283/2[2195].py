# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List


class Solution2:
    """超时"""

    def minimalKSum(self, nums: List[int], k: int) -> int:
        d = set()
        for x in nums:
            d.add(x)
        i = 1
        ans = 0
        while True:
            if k == 0:
                return ans
            if i not in d:
                ans += i
                k -= 1
            i += 1


class Solution:
    """数学"""
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 0
        for i, x in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if x <= k:
                k += 1
                ans -= x
        ans += (1 + k) * k // 2
        return ans


# nums = [1, 4, 25, 10, 25]
# k = 2
# print(Solution().minimalKSum(nums, k))
# nums = [5, 6]
# k = 6
# print(Solution().minimalKSum(nums, k))
# nums = [1]
# k = 100000000
# print(Solution().minimalKSum(nums, k))
nums = [96,44,99,25,61,84,88,18,19,33,60,86,52,19,32,47,35,50,94,17,29,98,22,21,72,100,40,84]
k = 35
print(Solution().minimalKSum(nums, k))