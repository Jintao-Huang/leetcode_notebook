# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        ans = []
        for i in range(len(points)):
            x = points[i]
            while len(ans) > 0 and x[0] <= ans[-1][1]:
                x = [max(ans[-1][0], x[0]), ans[-1][-1]]
                ans.pop()
            ans.append(x)
        return len(ans)


class Solution2:
    """空间压缩"""

    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        end = points[0][1]
        ans = 1
        for i in range(1, len(points)):
            x = points[i]
            if x[0] > end:
                ans += 1
                end = x[1]
        return ans


points = [[1, 2], [3, 4], [5, 6], [7, 8]]
points = [[1, 2], [3, 4], [1, 4]]
print(Solution().findMinArrowShots(points))
print(Solution2().findMinArrowShots(points))
