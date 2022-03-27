# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 
from typing import List


class Solution:
    def __init__(self):
        self.ans = []

    def _dfs(self, n: int, path: List[int], k: int, i: int) -> None:
        if k - len(path) > n + 1 - i:  # 剪枝
            return
        if len(path) == k:
            self.ans.append(path.copy())
            return
        for x in range(i, n + 1):
            path.append(x)
            self._dfs(n, path, k, x + 1)
            path.pop()

    def combine(self, n: int, k: int) -> List[List[int]]:
        self._dfs(n, [], k, 1)
        return self.ans


print(Solution().combine(4, 4))
