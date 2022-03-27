# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List


class Solution:
    """贪心. Ot(N) Os(1)"""

    # 选下一步最远的

    def jump(self, nums: List[int]) -> int:
        # 选择: 选/不选
        if len(nums) == 1:
            return 0
        ans = 1
        lo = 0  # idx
        max_pos = lo  # idx[from]
        for hi in range(len(nums)):
            if hi > nums[lo] + lo:
                lo = max_pos
                ans += 1
            #
            if nums[max_pos] + max_pos < nums[hi] + hi:
                max_pos = hi
        return ans


class Solution2:
    """动态规划"""

    def jump(self, nums: List[int]) -> int:
        # choice: nums[i]
        dp = [int(1e8)] * len(nums)
        dp[-1] = 0
        for i in reversed(range(len(nums) - 1)):
            for j in range(1, nums[i] + 1):
                if i + j >= len(dp):
                    break
                dp[i] = min(dp[i], dp[i + j] + 1)
        return dp[0]


nums = [7, 0, 9, 6, 9, 6, 1, 7, 9, 0, 1, 2, 9, 0, 3]
# nums = [2,1]
print(Solution().jump(nums))
print(Solution2().jump(nums))
