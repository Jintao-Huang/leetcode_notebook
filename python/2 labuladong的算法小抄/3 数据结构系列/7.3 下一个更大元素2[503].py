# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 
from typing import List


# 更大元素: 递减栈
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        s = []  # 索引
        ans = [-1] * len(nums)
        for i in range(2 * len(nums)):  # 循环
            ii = i % len(nums)
            x = nums[ii]
            while len(s) > 0 and x > nums[s[-1]]:  # s中有相同数字
                ans[s.pop()] = x
            s.append(ii)

        return ans


nums = [1, 2, 1]
print(Solution().nextGreaterElements(nums))
