# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 选择: 对j增(j<i); 不增
        # dp_N^2[i]: 以i结尾, 最长严格递增子序列长度
        # dp_N^2[i]; dp_N^2[0:i+1]
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


def lower_bound(nums, target):
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] >= target:
            hi = mid
        else:
            lo = mid + 1
    return lo


from bisect import bisect_left


class Solution2:
    # 堆顶数 递增
    # 每堆: 非增
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = []
        for i in range(len(nums)):
            idx = bisect_left(ans, nums[i])
            # idx = lower_bound(ans, nums[i])
            if idx < len(ans):
                ans[idx] = nums[i]
            else:
                ans.append(nums[i])

        return len(ans)


nums = [10, 9, 2, 5, 3, 7, 101, 18]
nums = [1, 3, 6, 7, 9, 4, 10, 5, 6]
print(Solution().lengthOfLIS(nums))
print(Solution2().lengthOfLIS(nums))
