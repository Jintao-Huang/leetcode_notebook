# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:

from typing import List, Set


class Solution:
    """回溯"""

    def __init__(self):
        self.rows = None
        self.cols = None
        self.boxes = None
        self.pos_list = None
        self.board = None

    def _solveSudoku(self, board, pos) -> bool:
        if pos == len(self.pos_list):
            return True

        i, j = self.pos_list[pos]
        bi = i // 3 * 3 + j // 3
        for x in self.rows[i].copy():
            if x in self.cols[j] or x in self.boxes[bi]:
                continue
            self.rows[i].remove(x)
            self.cols[j].add(x)
            self.boxes[bi].add(x)
            self.board[i][j] = str(x)

            if self._solveSudoku(board, pos + 1):
                return True
            self.rows[i].add(x)
            self.cols[j].remove(x)
            self.boxes[bi].remove(x)
            # self.board无需操作
        return False

    def solveSudoku(self, board: List[List[str]]) -> None:
        self.rows = [set(range(1, 10)) for _ in range(9)]  # type: List[Set[int]]  # 剩下的数字
        self.cols = [set() for _ in range(9)]  # type: List[Set[int]]  # 不能填的数字
        self.boxes = [set() for _ in range(9)]  # type: List[Set[int]]  # 不能填的数字
        # 找缺失的位置
        self.pos_list = []
        self.board = board
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    self.pos_list.append((i, j))
                else:
                    x = int(board[i][j])
                    bi = i // 3 * 3 + j // 3
                    self.rows[i].remove(x)
                    self.cols[j].add(x)
                    self.boxes[bi].add(x)

        self._solveSudoku(self.board, 0)


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

Solution().solveSudoku(board)
print(board)


class Solution2:
    """想法:
    1. 随机算法. Las Vegas; 选出某块所有能填的数, 随机填一个. : 大概率不行. 因为八皇后有很多个解, 数独的解很少.
    2. 优先填数少的行/列/块. : 可行"""
