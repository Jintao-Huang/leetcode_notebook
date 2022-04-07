# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # dp[i][j]: nums[i:j+1]能获得硬币最大数量
        # dp[i][j]: max(dp[i][k], dp[k][j])
        # 选(i, j)中一个气球戳.
        nums = [1] + nums + [1]
        dp = [[0] * len(nums) for i in range(len(nums))]
        for i in reversed(range(len(nums))):
            for j in range(i + 2, len(nums)):
                for k in range(i + 1, j):
                    dp[i][j] = max(
                        dp[i][j], dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j]
                    )
        return dp[0][len(nums) - 1]


print(Solution().maxCoins([3, 1, 5, 8]))
