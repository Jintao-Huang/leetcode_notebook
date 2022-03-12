# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List, Tuple


class Solution:
    """前缀和"""

    def shortestSubarray(self, nums: List[int], k: int) -> int:
        s = [0]
        for i in range(len(nums)):
            s.append(s[-1] + nums[i])
        print(s)
        stack = []
        ans = int(1e8)
        lo = 0
        for hi in range(1, len(s)):
            # shrink: nums[hi] - nums[lo] >= k

            while s[hi] - s[lo] >= k:
                ans = min(ans, hi - lo)
                while len(stack) > 0 and s[lo] >= stack[-1]:
                    stack.pop()
                stack.append(s[lo])
                lo += 1
        ans = min(ans, hi - lo)
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
nums = [84,-37,32,40,95]
k = 167
print(Solution().shortestSubarray(nums, k))
