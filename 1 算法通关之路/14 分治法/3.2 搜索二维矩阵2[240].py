# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List


class Solution:
    """贪心. Ot(N+M) Os(1)"""

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1
        while i <= m - 1 and j >= 0:
            x = matrix[i][j]
            if target == x:
                return True
            elif target < x:
                j -= 1
            else:
                i += 1
        return False


matrix = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]]
target = 5

# matrix =[[-1,3]]
# target = 3
print(Solution().searchMatrix(matrix, target))
