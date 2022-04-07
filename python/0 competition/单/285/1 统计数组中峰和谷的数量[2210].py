# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List
from collections import deque

class Solution:

    def countHillValley(self, nums: List[int]) -> int:
        dp_0 = [0] * len(nums)  # 增1, 减-1, 边界0
        dp_1 = [0] * len(nums)
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                dp_0[i] = 1
            elif nums[i] < nums[i -  1]:
                dp_0[i] = -1
            else:
                dp_0[i] = dp_0[i - 1]
        ans = 0
        for i in reversed(range(len(nums) - 1)):
            if nums[i] > nums[i + 1] and dp_0[i] == 1:
                ans += 1
            elif nums[i] < nums[i +  1] and dp_0[i] == -1:
                ans += 1
        return ans

nums = [2,4,1,1,6,5]
print(Solution().countHillValley(nums))

nums = [6,6,5,5,4,1]
print(Solution().countHillValley(nums))
