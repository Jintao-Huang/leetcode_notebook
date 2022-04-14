# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # C: 之前的每个数
        # S: [i]. 以i结束, 长度
        # dp_N^2[i]; dp_N^2[i-k]
        dp = [1] * len(nums)
        dp2 = [1] * len(nums)  #
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 == dp[i]:
                        dp2[i] += dp2[j]
                    elif dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        dp2[i] = dp2[j]

        max_ = max(dp)
        ans = 0
        for i in range(len(dp2)):
            if dp[i] == max_:
                ans += dp2[i]

        return ans


# print(Solution().findNumberOfLIS([1, 2, 4, 3, 5, 4, 7, 2]))
# print(Solution().findNumberOfLIS([2, 2, 2, 2, 2]))
print(Solution().findNumberOfLIS([1, 2, 3, 1, 2, 3, 1, 2, 3]))
