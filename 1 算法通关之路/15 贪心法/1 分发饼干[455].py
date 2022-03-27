# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List


class Solution:
    """贪心. Ot(NLogN MLogM)"""

    # 大的糖果满足不了, 小的糖果一定满足不了
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i, j = 0, 0
        ans = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                ans += 1
                i += 1
            j += 1

        return ans


g = [1, 2]
s = [1, 2, 3]
print(Solution().findContentChildren(g, s))
