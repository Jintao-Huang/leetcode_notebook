# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:

from typing import List
from python.template.data_structure.union_find import UnionFind


class Solution:
    """DFS递归. Ot(N) Os(N). 其中N为格子数"""

    def _dfs(self, i: int, j: int, grid: List[List[str]]) -> None:
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        n1, n2 = len(grid), len(grid[0])
        for d in directions:
            pi, pj = i + d[0], j + d[1]
            if 0 <= pi < n1 and 0 <= pj < n2:
                if grid[pi][pj] == "1":
                    grid[pi][pj] = "0"
                    self._dfs(pi, pj, grid)

    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        n1, n2 = len(grid), len(grid[0])
        for i in range(n1):
            for j in range(n2):
                if grid[i][j] == "1":
                    ans += 1
                    grid[i][j] = "0"
                    self._dfs(i, j, grid)
        return ans


class Solution2:
    """DFS迭代. Ot(N) Os(N). 其中N为格子数
    空间复杂度可优化: 去除visited. """

    def _dfs(self, i: int, j: int,
             grid: List[List[str]], visited: List[List[bool]]) -> None:
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        n1, n2 = len(grid), len(grid[0])
        stack = [(i, j)]  # type: List[Tuple[int, int]]
        while len(stack) > 0:
            i, j = stack.pop()
            for d in directions:
                pi, pj = i + d[0], j + d[1]
                if 0 <= pi < n1 and 0 <= pj < n2:
                    if not visited[pi][pj] and grid[pi][pj] == "1":
                        visited[pi][pj] = True
                        stack.append((pi, pj))

    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        n1, n2 = len(grid), len(grid[0])
        visited = [[False for _ in range(n2)] for _ in range(n1)]  # type: List[List[bool]]
        for i in range(n1):
            for j in range(n2):
                if not visited[i][j] and grid[i][j] == "1":
                    ans += 1
                    visited[i][j] = True
                    self._dfs(i, j, grid, visited)
        return ans


from collections import deque
from typing import Deque, Tuple


class Solution3:
    """BFS. Ot(N) Os(N)
    空间复杂度可优化: 去除visited. Os(短边)"""

    def _bfs(self, i: int, j: int,
             grid: List[List[str]], visited: List[List[bool]]) -> None:
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        n1, n2 = len(grid), len(grid[0])
        #
        visited[i][j] = True
        q = deque([(i, j)])  # type: Deque[Tuple[int, int]]
        while len(q) > 0:
            i, j = q.popleft()
            for d in directions:
                pi, pj = i + d[0], j + d[1]
                if 0 <= pi < n1 and 0 <= pj < n2:
                    if not visited[pi][pj] and grid[pi][pj] == "1":
                        visited[pi][pj] = True
                        q.append((pi, pj))

    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        n1, n2 = len(grid), len(grid[0])
        visited = [[False for _ in range(n2)] for _ in range(n1)]  # type: List[List[bool]]
        for i in range(n1):
            for j in range(n2):
                if not visited[i][j] and grid[i][j] == "1":
                    ans += 1
                    self._bfs(i, j, grid, visited)
        return ans



class Solution4:
    """Union Set. Ot(N) Os(N). find和union复杂度接近Ot(1)"""


    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        n, m = len(grid), len(grid[0])
        uf = UnionFind(n * m)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "0":
                    ans -= 1
                    continue
                base = i * m + j
                if j != m - 1 and grid[i][j +1] == '1':
                    right = base + 1
                    uf.union(base, right)
                if i != n-1 and grid[i + 1][j] == '1':
                    down = base + m
                    uf.union(base, down)

        return uf.cnt + ans


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]

print(Solution().numIslands(grid))
grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
print(Solution2().numIslands(grid))
grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
print(Solution3().numIslands(grid))
grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
print(Solution4().numIslands(grid))
