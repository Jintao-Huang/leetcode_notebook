# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List


class Solution:
    """常规方法: Ot(MN) Ot(MN). M: 行, N: 列"""

    def gameOfLife(self, board: List[List[int]]) -> None:
        b_ori = [b.copy() for b in board]
        n1, n2 = len(b_ori), len(b_ori[0])
        pos_list = [(-1, -1), (1, 1), (-1, 1), (1, -1),
                    (0, 1), (1, 0), (0, -1), (-1, 0)]
        for i in range(n1):
            for j in range(n2):
                n_alive = 0
                for p in pos_list:
                    ii, jj = i + p[0], j + p[1]
                    if ii < 0 or jj < 0 or ii >= n1 or jj >= n2:
                        continue
                    if b_ori[ii][jj] == 1:
                        n_alive += 1

                if b_ori[i][j] == 0:  # 死
                    if n_alive == 3:
                        board[i][j] = 1
                else:
                    if n_alive < 2 or n_alive > 3:
                        board[i][j] = 0


board = [[1, 1], [1, 0]]
Solution().gameOfLife(board)
print(board)


class Solution2:
    """原地/两次遍历法: Ot(MN) Os(1)"""

    def gameOfLife(self, board: List[List[int]]) -> None:
        n1, n2 = len(board), len(board[0])
        pos_list = [(-1, -1), (1, 1), (-1, 1), (1, -1),
                    (0, 1), (1, 0), (0, -1), (-1, 0)]
        # 0: 死
        # 1: 活
        # 2: 死, 下一步活
        # 3: 活, 下一步死
        for i in range(n1):
            for j in range(n2):
                n_alive = 0
                for p in pos_list:
                    ii, jj = i + p[0], j + p[1]
                    if ii < 0 or jj < 0 or ii >= n1 or jj >= n2:
                        continue
                    if board[ii][jj] == 1 or board[ii][jj] == 3:
                        n_alive += 1

                if board[i][j] == 0:  # 死
                    if n_alive == 3:
                        board[i][j] = 2
                else:  # == 1
                    if n_alive < 2 or n_alive > 3:
                        board[i][j] = 3
        #
        for i in range(n1):
            for j in range(n2):
                if board[i][j] == 2:
                    board[i][j] = 1
                if board[i][j] == 3:
                    board[i][j] = 0


board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
Solution2().gameOfLife(board)
print(board)
