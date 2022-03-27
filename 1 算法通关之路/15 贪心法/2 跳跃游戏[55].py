# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List


class Solution:
    """贪心/动态规划-空间优化. Ot(N) Os(1)"""
    # 选下一步最远的

    def canJump(self, nums: List[int]) -> bool:
        # 选择: 选/不选
        idx = nums[0]  # 最远(前面的)
        for i in range(1, len(nums)):
            if idx < i:
                return False
            idx = max(idx, i + nums[i])

        return True


nums = [2, 0, 0]
print(Solution().canJump(nums))
nums = [0, 1]
print(Solution().canJump(nums))


class Solution2:
    """动态规划. Ot(N) Os(N)"""

    def canJump(self, nums: List[int]) -> bool:
        # dp[i]: 以i结束, 最大可跳最远距离.
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            if dp[i - 1] < i:
                return False
            dp[i] = max(dp[i - 1], i + nums[i])
        return True


nums = [2, 0, 0]
print(Solution2().canJump(nums))
nums = [0, 1]
print(Solution2().canJump(nums))
