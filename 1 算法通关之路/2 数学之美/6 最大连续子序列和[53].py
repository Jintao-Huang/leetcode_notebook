# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List, Tuple, Dict


class Solution:
    """分治法. Ot(NLogN) Os(LogN)"""

    def _maxSubArray(self, nums: List[int], lo: int, hi: int) -> int:
        """[lo...hi]"""
        if lo > hi:
            return int(-1e9)  # !
        mid = (lo + hi) // 2
        x1 = self._maxSubArray(nums, lo, mid - 1)
        x3 = self._maxSubArray(nums, mid + 1, hi)
        #
        s1 = max_s1 = 0
        for i in range(mid - 1, lo - 1, -1):
            s1 += nums[i]
            max_s1 = max(s1, max_s1)
        #
        s2 = max_s2 = 0
        for i in range(mid + 1, hi + 1):
            s2 += nums[i]
            max_s2 = max(s2, max_s2)
        x2 = max_s1 + nums[mid] + max_s2
        return max(x1, x2, x3)

    def maxSubArray(self, nums: List[int]) -> int:
        return self._maxSubArray(nums, 0, len(nums) - 1)


class Solution2:
    """搜索. Ot(N) Os(N)."""

    def __init__(self):
        self.dp = {}  # 可改为数组
        self.nums = None

    def _dp(self, i: int) -> int:
        if i in self.dp:
            return self.dp[i]

        if i == 0:
            return nums[i]

        self.dp[i] = max(self._dp(i - 1), 0) + self.nums[i]
        return self.dp[i]

    def maxSubArray(self, nums: List[int]) -> int:
        self.nums = nums
        return max(self._dp(i) for i in range(len(nums)))


class Solution3:
    """动态规划. Ot(N) Os(N). 空间复杂度可降为Os(1)"""

    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(dp)):
            dp[i] = max(dp[i - 1], 0) + nums[i]

        return max(dp)


class Solution4:
    """前缀和. Ot(N) Os(1)."""

    def maxSubArray(self, nums: List[int]) -> int:
        s_min = 0
        s = 0
        ans = nums[0]
        #
        for i in range(len(nums)):
            s += nums[i]
            # 注意顺序!
            ans = max(ans, s - s_min)
            s_min = min(s_min, s)

        return ans


nums = [-1]
print(Solution().maxSubArray(nums))
print(Solution2().maxSubArray(nums))
print(Solution3().maxSubArray(nums))
print(Solution4().maxSubArray(nums))
