# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n, m = len(matrix), len(matrix[0])
        self.s = [[0] * (m + 1)]  # (n+1) * (m+1)
        for i in range(n):
            self.s.append([0])
            for j in range(m):
                self.s[i + 1].append(self.s[i + 1][j] + self.s[i][j + 1] - self.s[i][j] + matrix[i][j])


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.s[row2 + 1][col2 + 1] - self.s[row2 + 1][col1] - self.s[row1][col2 + 1] + self.s[row1][col1]




from template.build.call_func import call_func

print(call_func(["NumMatrix", "sumRegion", "sumRegion", "sumRegion"],
                [[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]],
                 [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]], globals()))