# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List
from template.utils.array import find


class Solution:
    """dfs"""

    def _dfs(self, arr: List[int], visited: List[bool], p: int, end: int) -> bool:
        # choice: 2
        x = arr[p]
        if x == 0:
            return True
        #
        ans = False
        if p - x >= 0 and not visited[p - x]:
            visited[p - x] = True
            ans |= self._dfs(arr, visited, p - x, end)
        if p + x < len(arr) and not visited[p + x]:
            visited[p + x] = True
            ans |= self._dfs(arr, visited, p + x, end)
        return ans

    def canReach(self, arr: List[int], start: int) -> bool:
        idx = find(arr, 0)
        # 从0跳到start
        visited = [False] * len(arr)
        visited[start] = True
        return self._dfs(arr, visited, start, idx)


arr = [4, 2, 3, 0, 3, 1, 2]
start = 5
print(Solution().canReach(arr, start))


class Solution2:
    """bfs"""
