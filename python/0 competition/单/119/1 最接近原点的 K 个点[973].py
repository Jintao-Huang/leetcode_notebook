# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List
from math import sqrt


class Solution:
    """自定义排序"""

    def get_dist(self, i, j) -> float:
        return sqrt(i ** 2 + j ** 2)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        d = [(self.get_dist(x, y), [x, y]) for x, y in points]
        d.sort()
        ans = []
        for i in range(k):
            ans.append(d[i][1])
        return ans


from heapq import nsmallest


class Solution2:
    """堆"""
    def get_dist(self, i, j) -> float:
        return sqrt(i ** 2 + j ** 2)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        d = [(self.get_dist(x, y), [x, y]) for x, y in points]
        ans = nsmallest(k, d)

        return [a[1] for a in ans]


points = [[1, 3], [-2, 2]]
k = 1
print(Solution().kClosest(points, k))
print(Solution2().kClosest(points, k))
