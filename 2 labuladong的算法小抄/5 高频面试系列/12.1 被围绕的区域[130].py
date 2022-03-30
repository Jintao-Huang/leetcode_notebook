# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:

from typing import List
from template.data_structure.union_find import UnionFind


class Solution:
    """union find"""
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        uf = UnionFind(m * n + 1)
        for i in range(m):
            for j in range(n):
                x = board[i][j]
                ij = i * n + j
                if x == 'O':
                    for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        p = i + d[0], j + d[1]
                        if p[0] < 0 or p[1] < 0 or p[0] >= m or p[1] >= n:
                            uf.union(ij, m * n)
                            continue
                        pp = p[0] * n + p[1]
                        if board[p[0]][p[1]] == 'O':
                            uf.union(ij, pp)

        for i in range(m):
            for j in range(n):
                x = board[i][j]
                ij = i * n + j
                if x == 'O' and uf.find(ij) != uf.find(m*n):
                    board[i][j] = 'X'

board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
board = [["O","O","O"],["O","O","O"],["O","O","O"]]
Solution().solve(board)
print(board)