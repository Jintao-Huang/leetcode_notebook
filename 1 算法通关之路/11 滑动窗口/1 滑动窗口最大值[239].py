# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:

from typing import List, Deque
from collections import deque


class Solution:
    """单调Deque, 准滑动窗口. Ot(N) Os(K)
    shrink条件: len==k
    shrink=True: ans"""

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        # 最近(迭代: 从远及近). [0]最大: 递减; 最小: 递增
        q = deque()  # type: Deque[int]  # 递减队列. 存索引
        #
        for hi in range(len(nums)):
            # 模板: 先hi, 后lo.
            while len(q) > 0 and nums[q[-1]] <= nums[hi]:
                q.pop()
            q.append(hi)
            # shrink省略
            lo = hi - k + 1
            if lo >= 0:
                # shrink
                ans.append(nums[q[0]])
                if q[0] == lo:
                    q.popleft()
                #
        return ans



nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(Solution().maxSlidingWindow(nums, k))
