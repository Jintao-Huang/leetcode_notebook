# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List, Set


class Solution:
    def __init__(self):
        self.ans: List[List[str]]

    @staticmethod
    def gen_board(path: List[int]) -> List[str]:
        n = len(path)
        s = "." * n
        ans = []
        for j in path:
            ans.append(s[:j] + 'Q' + s[j + 1:])
        return ans

    def _dfs(self, n: int, path: List[int],
             col_s: Set[int], ld_s: Set[int], rd_s: Set[int]):
        # 选择: 位置
        i = len(path)
        if i == n:
            self.ans.append(self.gen_board(path))
            return

        for j in range(n):
            if (j in col_s) or (i - j in ld_s) or (i + j in rd_s):
                continue
            col_s.add(j)
            ld_s.add(i - j)
            rd_s.add(i + j)
            path.append(j)
            self._dfs(n, path, col_s, ld_s, rd_s)
            col_s.remove(j)
            ld_s.remove(i - j)
            rd_s.remove(i + j)
            path.pop()

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.ans = []
        self._dfs(n, [], set(), set(), set())
        return self.ans


print(Solution().solveNQueens(4))
