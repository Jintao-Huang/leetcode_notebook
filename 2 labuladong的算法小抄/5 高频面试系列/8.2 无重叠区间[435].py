# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List


class Solution:
    """贪心. 相反面: 最大不重叠区间. Ot(NLogN)"""

    # ii没重叠, 前面的都不会重叠
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        ans = 0
        end = int(-1e8)
        for i in range(len(intervals)):
            ii = intervals[i]
            if ii[0] >= end:
                ans += 1
                end = ii[1]
        return len(intervals) - ans


intervals = [[1, 100], [11, 22], [1, 11], [2, 12]]
print(Solution().eraseOverlapIntervals(intervals))
intervals = [[1, 2], [2, 3], [3, 4], [-100, -2], [5, 7]]
print(Solution().eraseOverlapIntervals(intervals))
