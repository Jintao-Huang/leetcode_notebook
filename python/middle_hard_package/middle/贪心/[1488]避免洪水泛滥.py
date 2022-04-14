# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 
from typing import List
from collections import defaultdict

from python.template.data_structure.sorted_list import SortedList


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        zero = SortedList()
        n = len(rains)
        full = defaultdict(int)
        res = [-1] * n
        for i in range(n):
            r = rains[i]
            if r == 0:
                zero.add(i)
                continue
            if r in full:
                idx = zero.bisect_right(full[r])
                if idx >= len(zero):
                    return []
                res[zero[idx]] = r
                zero.pop(idx)
            full[r] = i

        for i in range(len(zero)):
            x = zero[i]
            res[x] = 1
        return res


# rains = [69, 0, 0, 0, 69]
rains = [1, 0, 2, 0, 3, 0, 2, 0, 0, 0, 1, 2, 3]
print(Solution().avoidFlood(rains))
# rains = [0, 1, 1]
# print(Solution().avoidFlood(rains))
