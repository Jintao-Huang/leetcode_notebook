# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

"""
https://leetcode-cn.com/problems/longest-increasing-subsequence/
300. 最长递增子序列
- 中等
- 推荐
=
- 动态规划
"""

from typing import List
from functools import lru_cache


class Solution:
    """dfs"""

    def lengthOfLIS(self, nums: List[int]) -> int:
        @lru_cache(len(nums) + 3)
        def _dp(i: int) -> int:
            """nums[0...i]以nums[i]结尾的LIS"""
            nonlocal nums
            if i == 0:
                return 1
            #
            ans = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    ans = max(ans, _dp(j) + 1)
            return ans

        #
        return max(_dp(i) for i in range(len(nums)))


nums = [1, 3, 6, 7, 9, 4, 10, 5, 6]
print(Solution().lengthOfLIS(nums))


class Solution2:
    """动态规划"""

    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n  # 含base
        #
        for i in range(1, n):
            #
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        #
        return max(dp)


nums = [1, 3, 6, 7, 9, 4, 10, 5, 6]
print(Solution2().lengthOfLIS(nums))

from bisect import bisect_left


class Solution3:
    """二分搜索. 了解即可"""

    def lengthOfLIS(self, nums: List[int]) -> int:
        top = []  # 存放每个堆的堆顶元素
        #
        for x in nums:
            idx = bisect_left(top, x)  # lower_bound()
            #
            if idx >= len(top):
                top.append(x)
            else:
                top[idx] = x
        #
        return len(top)


nums = [1, 3, 6, 7, 9, 4, 10, 5, 6]
print(Solution3().lengthOfLIS(nums))
