# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List

class Solution:
    """动态规划优化. Ot(N) Os(1)"""
    def rob(self, nums: List[int]) -> int:
        x, y = 0, nums[0]  # 不抢, 抢
        for i in range(1, len(nums)):
            x, y = max(x, y), x + nums[i]
        return max(x, y)


print(Solution().rob([1, 3, 1, 3, 100]))