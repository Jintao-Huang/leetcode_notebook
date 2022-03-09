# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:

from typing import List


class Solution:
    """原地. Ot(N^2) Os(1)"""

    def set_row_zero(self, mat, i):
        for j in range(len(mat[0])):
            mat[i][j] = 0

    def set_col_zero(self, mat, j):
        for i in range(len(mat)):
            mat[i][j] = 0

    def setZeroes(self, matrix: List[List[int]]) -> None:
        set_first_col_zero = False
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                set_first_col_zero = True
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for j in range(1, len(matrix[0])):
            if matrix[0][j] == 0:
                self.set_col_zero(matrix, j)

        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                self.set_row_zero(matrix, i)

        if set_first_col_zero:
            self.set_col_zero(matrix, 0)


class Solution2:
    def set_row_None(self, mat, i):
        for j in range(len(mat[0])):
            if mat[i][j] != 0:
                mat[i][j] = None

    def set_col_None(self, mat, j):
        for i in range(len(mat)):
            if mat[i][j] != 0:
                mat[i][j] = None

    def setZeroes(self, matrix: List[List[int]]) -> None:
        # None: now: X, next: 0
        # 0: now: 0, next: 0
        # 其他X: now: X, next: X
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    self.set_row_None(matrix, i)
                    self.set_col_None(matrix, j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] is None:
                    matrix[i][j] = 0


matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
Solution().setZeroes(matrix)
print(matrix)
matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
Solution2().setZeroes(matrix)
print(matrix)
