# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List
from collections import defaultdict

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        d = defaultdict(int)
        for m in matches:
            d[m[1]] += 1
            if m[0] not in d:
                d[m[0]] = 0

        ans = [[],[]]
        for k, v in d.items():
            if v == 0:
                ans[0].append(k)
            elif v == 1:
                ans[1].append(k)
        ans[0].sort()
        ans[1].sort()
        return ans


