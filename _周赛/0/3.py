# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # nums[i:j+1] 可被k整除:
        # 即: nums[:j+1], nums[:i-1]的余数相同
        # dp[i]: 余数为i的前缀和数量. 已经过动态规划-空间优化
        dp = [0] * k
        dp[0] = 1
        s = 0
        ans = 0
        for x in nums:
            s += x
            mod = s % k
            if mod not in dp:
                dp[mod] = 0
            ans += dp[mod]
            dp[mod] += 1
        return ans


nums = [4, 5, 0, -2, -3, 1]
k = 5


class Solution2:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # nums[i:j+1] 可被k整除:
        # 即: nums[:j+1], nums[:i-1]的余数相同
        d = {0: 1}
        s = 0
        ans = 0
        for x in nums:
            s += x
            y = s % k
            if y not in d:
                d[y] = 0
            ans += d[y]

            d[y] += 1
        return ans


print(Solution2().subarraysDivByK(nums, k))
