# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List


class Solution:
    """贪心+栈"""

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[1])
        ans = []
        for x in intervals:
            while len(ans) > 0 and x[0] <= ans[-1][1]:
                x = [min(ans[-1][0], x[0]), x[1]]
                ans.pop()
            ans.append(x)
        return ans


intervals = [[1, 2], [3, 4], [1, 4]]
print(Solution().merge(intervals))

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(Solution().merge(intervals))
intervals = [[1, 4], [0, 4]]
print(Solution().merge(intervals))
intervals = [[1, 4], [2, 3]]
print(Solution().merge(intervals))
