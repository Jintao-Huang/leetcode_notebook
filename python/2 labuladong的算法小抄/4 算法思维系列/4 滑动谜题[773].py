# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List
from collections import deque
from copy import deepcopy


class Solution:

    def slidingPuzzle(self, board: List[List[int]]) -> int:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 0:
                    pos = i, j
                    break
        #
        visited = {str(board)}
        end = str([[1, 2, 3], [4, 5, 0]])
        if end in visited:
            return 0
        q = deque([(board, pos)])
        ans = 1
        while len(q) > 0:
            for _ in range(len(q)):
                board, pos = q.popleft()
                for d in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                    n = pos[0] + d[0], pos[1] + d[1]
                    if n[0] < 0 or n[0] >= len(board) \
                            or n[1] < 0 or n[1] >= len(board[0]):
                        continue
                    b = deepcopy(board)
                    b[pos[0]][pos[1]], b[n[0]][n[1]] = b[n[0]][n[1]], b[pos[0]][pos[1]]
                    b_str = str(b)
                    if b_str == end:
                        return ans
                    if b_str not in visited:
                        q.append((b, n))
                        visited.add(b_str)
            ans += 1
        return -1


class Solution2:

    def slidingPuzzle(self, board: List[List[int]]) -> int:
        neighbor = [[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3, 5], [2, 4]]
        board = [str(x) for b in board for x in b]
        for i in range(len(board)):
            if board[i] == '0':
                pos = i
                break
        #
        visited = {"".join(board)}
        end = str("123450")
        if end in visited:
            return 0
        q = deque([(board, pos)])
        ans = 1
        while len(q) > 0:
            for _ in range(len(q)):
                board, pos = q.popleft()
                for p2 in neighbor[pos]:
                    if p2 < 0 or p2 >= len(board):
                        continue
                    b = board.copy()
                    b[pos], b[p2] = b[p2], b[pos]
                    b_str = "".join(b)
                    if b_str == end:
                        return ans
                    if b_str not in visited:
                        q.append((b, p2))
                        visited.add(b_str)
            ans += 1
        return -1


# print(Solution().slidingPuzzle([[1, 2, 3], [4, 0, 5]]))
# print(Solution().slidingPuzzle([[1, 2, 3], [5, 4, 0]]))
print(Solution().slidingPuzzle([[4, 1, 2], [5, 0, 3]]))
print(Solution2().slidingPuzzle([[4, 1, 2], [5, 0, 3]]))
