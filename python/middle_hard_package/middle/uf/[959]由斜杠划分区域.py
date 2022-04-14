# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:
from typing import List
from python.template.data_structure.union_find import UnionFind


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n, m = len(grid), len(grid[0])
        uf = UnionFind(4 * n * m)
        for i in range(n):
            for j in range(m):
                c = grid[i][j]
                # 上0, 顺时针-3
                base = 4 * (i * m + j)
                if c == "\\":
                    uf.union(base, base + 1)
                    uf.union(base + 2, base + 3)
                elif c == '/':
                    uf.union(base, base + 3)
                    uf.union(base + 1, base + 2)
                else:
                    uf.union(base, base + 1)
                    uf.union(base + 1, base + 2)
                    uf.union(base + 2, base + 3)
                # 跨
                if j != m - 1:
                    right = base + 4
                    uf.union(base + 1, right + 3)
                if i != n - 1:
                    down = base + 4 * m
                    uf.union(base + 2, down)
        return uf.cnt


grid = ["/\\", "\\/"]
print(Solution().regionsBySlashes(grid))
