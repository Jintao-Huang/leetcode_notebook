# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List
from heapq import nsmallest


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        arr = []
        for i in range(len(matrix)):
            arr.extend(matrix[i])
        return nsmallest(k, arr)[-1]


matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
k = 8
print(Solution().kthSmallest(matrix, k))
