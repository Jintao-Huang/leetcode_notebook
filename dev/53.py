# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

"""
https://leetcode-cn.com/problems/maximum-subarray/
53. 最大子序和
- 简单
- 推荐
=
- 动态规划
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        # dp[i]: nums[0...i]以nums[i]结尾的最大子数组和
        dp = nums.copy()  # dp[0]: base
        #
        for i in range(1, n):
            #
            if dp[i - 1] > 0:
                dp[i] += dp[i - 1]
        return max(dp)

    def maxSubArray2(self, nums: List[int]) -> int:
        """状态压缩"""
        n = len(nums)
        if n == 0:
            return 0
        #
        ans = dp = nums[0]
        #
        for i in range(1, len(nums)):
            #
            dp = nums[i] + max(0, dp)
            ans = max(ans, dp)
        return ans


nums = [1]
print(Solution().maxSubArray(nums))
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(Solution().maxSubArray(nums))
#
nums = [1]
print(Solution().maxSubArray2(nums))
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(Solution().maxSubArray2(nums))
