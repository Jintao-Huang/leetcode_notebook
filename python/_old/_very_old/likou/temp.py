# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:
from typing import List


class Solution:
    """300. 最长递增子序列"""

    def lengthOfLIS(self, nums: List[int]) -> int:
        """动态规划. Ot(N^2) Os(N)"""
        length = len(nums)
        dp = [1] * length
        for i in range(length):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(Solution().lengthOfLIS(nums))  # 4
