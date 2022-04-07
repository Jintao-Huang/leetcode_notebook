# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

# 链表那题

from collections import defaultdict
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        ans = 0
        d = defaultdict(int)
        for c in s:
            d[c] += 1

        for c in t:
            if d[c] == 0:
                ans += 1
            else:
                d[c] -= 1
        for v in d.values():
            ans += v
        return ans


