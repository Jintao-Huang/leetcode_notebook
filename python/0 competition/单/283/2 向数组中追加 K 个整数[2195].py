# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List


class Solution:
    """排序. 注意: 避免相同的数"""

    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums += [0, int(2e9)]
        nums.sort()
        ans = 0
        for i in range(len(nums) - 1):
            if k == 0:
                break
            diff = min(nums[i + 1] - nums[i] - 1, k)
            if diff > 0:
                ans += (nums[i] * 2 + diff + 1) * diff // 2
                k -= diff
        return ans


nums = [1, 4, 2, 2, 25, 10, 25]
k = 2
print(Solution().minimalKSum(nums, k))
# nums = [5, 6]
# k = 6
# print(Solution().minimalKSum(nums, k))
# nums = [1]
# k = 100000000
# print(Solution().minimalKSum(nums, k))
nums = [96, 44, 99, 25, 61, 84, 88, 18, 19, 33, 60, 86, 52, 19, 32, 47, 35, 50, 94, 17, 29, 98, 22, 21, 72, 100, 40, 84]
k = 35
print(Solution().minimalKSum(nums, k))
