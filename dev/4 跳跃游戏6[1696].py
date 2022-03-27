# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List
from collections import deque


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        #
        ans = [None] * len(nums)
        q = deque()  # 递减队列. 存索引. 可存数
        #
        for lo in reversed(range(len(nums))):
            if len(q) > 0 and q[0] - lo > k:  # !
                q.popleft()
            if len(q) > 0:  #
                ans[lo] = nums[q[0]]
                nums[lo] += nums[q[0]]
            # !
            while len(q) > 0 and nums[lo] >= nums[q[-1]]:
                q.pop()
            q.append(lo)  # 含hi.
            #
        return nums[0]


nums = [1, -1, -2, 4, -7, 3]
k = 2
print(Solution().maxResult(nums, k))
