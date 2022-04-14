# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 


from python.template.data_structure.union_find import UnionFind

from typing import List


class Solution:
    """Union Set. find和union复杂度接近Ot(1). Ot(P) Os(N). P=len(positions)"""

    def _union_set(self, uf: UnionFind, i: int, j: int, grid: List[List[int]]) -> int:
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        n1, n2 = len(grid), len(grid[0])
        union_num = 0
        for d in directions:
            pi, pj = i + d[0], j + d[1]
            if 0 <= pi < n1 and 0 <= pj < n2:
                if grid[pi][pj] == 1:
                    if uf.union(i * n2 + j, pi * n2 + pj):
                        union_num += 1
        return union_num

    def numIslands(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        ans = []
        a = 0
        uf = UnionFind(m * n)
        grid = [[0 for _ in range(n)] for _ in range(m)]  # type: List[List[int]]
        for i, j in positions:
            grid[i][j] = 1
            a += 1
            a -= self._union_set(uf, i, j, grid)
            ans.append(a)
        return ans


print(Solution().numIslands(3, 3, [[0, 0], [0, 2], [1, 1], [0, 1]]))
# [1, 2, 3, 1]
