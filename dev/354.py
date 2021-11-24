# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

"""
https://leetcode-cn.com/problems/russian-doll-envelopes/
354. 俄罗斯套娃信封问题
- 困难
=
- 动态规划
"""
from typing import List


class Solution:
    """动态规划"""

    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        dp = [1] * n
        envelopes = sorted(envelopes)
        #
        for i in range(n):
            #
            for j in range(i):
                if envelopes[j][0] < envelopes[i][0] and envelopes[j][1] < envelopes[i][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        #
        return max(dp)

    def _lengthOfLIS(self, nums: List[int]) -> int:
        """copy from 300"""
        n = len(nums)
        dp = [1] * n
        #
        for i in range(n):
            #
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        #
        return max(dp)

    def maxEnvelopes2(self, envelopes: List[List[int]]) -> int:
        """有技巧的排序"""
        envelopes = sorted(envelopes, key=lambda env: (env[0], -env[1]))
        h = [env[1] for env in envelopes]  # w, h 取 h
        #
        return self._lengthOfLIS(h)


envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
print(Solution().maxEnvelopes(envelopes))
print(Solution().maxEnvelopes2(envelopes))

from bisect import bisect_left


class Solution:
    """二分查找"""

    def _lengthOfLIS(self, nums: List[int]) -> int:
        """copy from 300"""
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

    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        """有技巧的排序"""
        envelopes = sorted(envelopes, key=lambda env: (env[0], -env[1]))
        h = [env[1] for env in envelopes]  # w, h 取 h
        #
        return self._lengthOfLIS(h)
