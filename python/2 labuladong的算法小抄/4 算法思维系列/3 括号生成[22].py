# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List


class Solution:
    """回溯法"""

    def __init__(self):
        self.ans = []
        self.n = 0

    def _dfs(self, path: List[str], le: int, ri: int) -> None:
        if le == 0 and ri == 0:
            self.ans.append("".join(path))
            return

        # 选择: 左, 右括号
        if le > 0:
            path.append('(')
            self._dfs(path, le - 1, ri)
            path.pop()
        #
        if ri > le:
            path.append(')')
            self._dfs(path, le, ri - 1)
            path.pop()

    def generateParenthesis(self, n: int) -> List[str]:
        self.n = n
        self._dfs([], n, n)
        return self.ans


print(Solution().generateParenthesis(3))
