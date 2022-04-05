# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        for i in reversed(range(1, len(nums))):
            for j in range(i):
                nums[j] = (nums[j] + nums[j + 1]) % 10
        return nums[0]


nums = [1,2,3,4,5]
print(Solution().triangularSum(nums))