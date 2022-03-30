# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List, Tuple

from collections import deque


class Solution:
    """前缀和+单调队列"""

    def shortestSubarray(self, nums: List[int], k: int) -> int:
        s = [0]
        for i in range(len(nums)):
            s.append(s[-1] + nums[i])
        ans = int(1e8)
        q = deque()  # 递增
        for hi in range(len(s)):
            x = s[hi]
            while len(q) > 0 and x <= s[q[-1]]:
                q.pop()
            while len(q) > 0 and x - s[q[0]] >= k:
                ans = min(ans, hi - q.popleft())
            q.append(hi)
        return ans if ans != int(1e8) else -1


# nums = [17, 85, 93, -45, -21]
# k = 150
# print(Solution().shortestSubarray(nums, k))
# nums = [1, 2]
# k = 4
# print(Solution().shortestSubarray(nums, k))
# nums = [1]
# k = 1
# print(Solution().shortestSubarray(nums, k))
nums = [84, -37, 32, 40, 95]
k = 167
print(Solution().shortestSubarray(nums, k))
