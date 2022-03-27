# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List


class Solution:
    """贪心+栈"""
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # `[`没超前面最大的`]`, 则前面的都不会超.
        intervals.sort(key=lambda x: x[1])
        ans = []
        for x in intervals:
            while len(ans) > 0:
                if x[0] <= ans[-1][1]:
                    ans[-1] = [min(ans[-1][0], x[0]), x[1]]
                    x = ans[-1]
                    ans.pop()
                else:
                    break
            ans.append(x)
        return ans


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(Solution().merge(intervals))
intervals = [[1, 4], [0, 4]]
print(Solution().merge(intervals))
intervals = [[1, 4], [2, 3]]
print(Solution().merge(intervals))
