# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:

from typing import List, Deque
from collections import deque


# 最近K个, j < i, argmax[j](nums[j]).
class Solution:
    """单调Deque. Ot(N) Os(K)"""

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        q = deque()  # 递减队列. 存索引. 可存数
        #
        for hi in range(len(nums)):
            while len(q) > 0 and nums[q[-1]] <= nums[hi]:
                q.pop()
            q.append(hi)  # 含hi.
            if len(q) > 0 and hi + 1 - q[0] > k:
                q.popleft()
            if hi + 1 - k >= 0:  # k >= 1
                ans.append(nums[q[0]])
        return ans


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(Solution().maxSlidingWindow(nums, k))
