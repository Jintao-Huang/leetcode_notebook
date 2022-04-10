# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List


class Solution:
    """动态规划. Ot(N) Os(N)"""

    def rob(self, nums: List[int]) -> int:
        # 选择: 选, 不选
        # dp_N^2[i]: 前i个nums(含)的偷窃最高金额
        # base: dp_N^2[0]=nums[0], dp_N^2[1]=max(nums[0],nums[1])
        # 转移: dp_N^2[i]=max(dp_N^2[i-2]+nums[i], dp_N^2[i-1])
        if len(nums) == 1:
            return nums[0]
        dp = [nums[0], max(nums[0], nums[1])]
        for i in range(2, len(nums)):
            t = max(dp[i - 2] + nums[i], dp[i - 1])
            dp.append(t)
        return dp[-1]


class Solution2:
    """动态规划-空间优化. Ot(N) Os(1)"""

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        x, y = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            x, y = y, max(x + nums[i], y)
        return y


nums = [2, 1]
print(Solution().rob(nums))
print(Solution2().rob(nums))
