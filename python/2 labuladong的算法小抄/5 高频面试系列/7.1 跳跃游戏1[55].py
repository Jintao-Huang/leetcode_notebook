# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List


class Solution:
    """贪心. Ot(N) Os(1)"""

    # 选下一步最远的

    def canJump(self, nums: List[int]) -> bool:
        # 选择: 选/不选
        idx = 0  # 拥有最远距离的点
        for i in range(1, len(nums)):
            if idx + nums[idx] < i:
                return False
            if idx + nums[idx] < i + nums[i]:
                idx = i
        return True


nums = [2, 0, 0]
print(Solution().canJump(nums))
nums = [0, 1]
print(Solution().canJump(nums))


class Solution2:
    """动态规划. Ot(N^2) Os(N)"""

    def canJump(self, nums: List[int]) -> bool:
        # dp_N^2[i]: 以i开始, 是否能跳到终点
        # 选择nums[i]个
        dp = [False] * len(nums)
        dp[-1] = True
        for i in reversed(range(len(nums) - 1)):
            for j in range(1, nums[i] + 1):
                if i + j >= len(dp):
                    break
                if dp[i + j] is True:
                    dp[i] = True
                    break
        return dp[0]


nums = [2, 0, 0]
print(Solution2().canJump(nums))
nums = [0, 1]
print(Solution2().canJump(nums))
