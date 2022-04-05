# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:
from typing import List

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        x = start ^ goal
        ans = 0
        for i in range(32):
            ans += x & 1
            x >>= 1
        return ans


start = 10
goal = 7
print(Solution().minBitFlips(start, goal))