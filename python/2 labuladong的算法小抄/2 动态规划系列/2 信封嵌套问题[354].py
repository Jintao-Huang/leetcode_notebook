# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:
from typing import List

from bisect import bisect_left


def lengthOfLIS(nums: List[int]) -> int:
    ans = []
    for i in range(len(nums)):
        idx = bisect_left(ans, nums[i])
        # idx = lower_bound(ans, nums[i])
        if idx < len(ans):
            ans[idx] = nums[i]
        else:
            ans.append(nums[i])

    return len(ans)


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda e: (e[0], -e[1]))
        return lengthOfLIS([e[1] for e in envelopes])


envelopes = [[4, 5], [4, 6], [6, 7], [2, 3], [1, 1]]
print(Solution().maxEnvelopes(envelopes))
